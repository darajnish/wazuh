#!/bin/bash
setup_directories() {
    local base_dir="$1"
    local src_dir="$2"
    local test_type="$3"
    echo "--- Folder creation ---"
    mkdir -p "$base_dir" "$base_dir/engine" "$base_dir/queue/sockets" "$base_dir/logs"

    if [ "$test_type" = "integration_test" ]; then

        local ruleset_dir="$src_dir/ruleset/wazuh-core-test"
        mkdir -p "$ruleset_dir/decoders" "$ruleset_dir/filters"
        echo "name: decoder/test-message/0" > "$ruleset_dir/decoders/test-message.yml"
        echo "name: filter/allow-all/0" > "$ruleset_dir/filters/allow-all.yml"
        cat <<- EOM > "$ruleset_dir/manifest.yml"
name: integration/wazuh-core-test/0
decoders:
  - decoder/test-message/0
EOM
    fi
}

load_integrations_policies() {
    local environment_dir="$1"
    local engine_src_dir="$2"
    local engine_dir="$3"

    echo "--- Loading ruleset & enabling wazuh environment  ---"
    local serv_conf_file="$engine_src_dir/test/integration_tests/configuration_files/general.conf"
    sed -i "s|github_workspace|$environment_dir|g" "$serv_conf_file"

    "$engine_src_dir/build/main" --config "$serv_conf_file" server -l error start &

    sleep 2

    # Capture the process ID of the binary
    local binary_pid=$!

    # Add filter for route
    "$engine_src_dir/build/main" catalog --api_socket $environment_dir/queue/sockets/engine-api -n system create filter < $engine_src_dir/ruleset/filters/allow-all.yml

    # Define source and destination directories
    source_dir="$engine_src_dir/ruleset/wazuh-core"
    destination_dir="$engine_src_dir/ruleset/wazuh-core-test"

    # Create the destination folder if it doesn't exist
    mkdir -p "$destination_dir"

    # Copy the contents of the wazuh-core folder to the destination
    cp -r "$source_dir"/* "$destination_dir"

    # Delete the "output" subfolder in wazuh-core-test
    rm -r "$destination_dir/outputs"

    cd $destination_dir
    engine-integration generate-manifest

    echo 'name: policy/wazuh/1
integrations:
    - integration/apache-http/0
    - integration/suricata/0
    - integration/syslog/0
    - integration/system/0
    - integration/wazuh-core-test/0
    - integration/windows/0' > "$engine_src_dir/ruleset/policy.yml"

    cd ..

    engine-integration add --api-sock $environment_dir/queue/sockets/engine-api -n system wazuh-core-test/
    engine-integration add --api-sock $environment_dir/queue/sockets/engine-api -n wazuh integrations/syslog/
    engine-integration add --api-sock $environment_dir/queue/sockets/engine-api -n wazuh integrations/system/
    engine-integration add --api-sock $environment_dir/queue/sockets/engine-api -n wazuh integrations/windows/
    engine-integration add --api-sock $environment_dir/queue/sockets/engine-api -n wazuh integrations/apache-http/
    engine-integration add --api-sock $environment_dir/queue/sockets/engine-api -n wazuh integrations/suricata/

    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api add -p policy/wazuh/1 -f
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api parent-set -p policy/wazuh/1 decoder/integrations/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api parent-set -p policy/wazuh/1 -n wazuh decoder/integrations/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api asset-add -p policy/wazuh/1 -n system integration/wazuh-core-test/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api asset-add -p policy/wazuh/1 -n wazuh integration/syslog/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api asset-add -p policy/wazuh/1 -n wazuh integration/system/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api asset-add -p policy/wazuh/1 -n wazuh integration/windows/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api asset-add -p policy/wazuh/1 -n wazuh integration/apache-http/0
    "$engine_src_dir/build/main" policy --api_socket $environment_dir/queue/sockets/engine-api asset-add -p policy/wazuh/1 -n wazuh integration/suricata/0

    "$engine_src_dir/build/main" router --api_socket $environment_dir/queue/sockets/engine-api add default filter/allow-all/0 255 policy/wazuh/1

    echo "Creating integrations of engine-test..."
     # TODO: think about a better way to do this, maybe save the default information in kvdb
    echo "{}" > $engine_dir/etc/engine-test.conf

    cd $engine_src_dir
    engine-test -c $engine_dir/etc/engine-test.conf add -i windows -f eventchannel
    engine-test -c $engine_dir/etc/engine-test.conf add -i syslog -f syslog -o /tmp/syslog.log
    engine-test -c $engine_dir/etc/engine-test.conf add -i remote-syslog -f remote-syslog -o 127.0.0.1
    engine-test -c $engine_dir/etc/engine-test.conf add -i suricata -f json
    engine-test -c $engine_dir/etc/engine-test.conf add -i system -f syslog

    rm -r "$destination_dir"
    rm -r "$engine_src_dir/ruleset/policy.yml"

    kill $binary_pid
}

setup_engine() {
    local src_dir="$1"
    local engine_dir="$2"
    echo "--- Setting up the engine ---"
    mkdir -p "$engine_dir/store/schema" "$engine_dir/etc/kvdb"
    local schemas=("wazuh-logpar-types" "wazuh-asset" "wazuh-policy" "engine-schema")
    for schema in "${schemas[@]}"; do
        mkdir -p "$engine_dir/store/schema/$schema"
        cp "$src_dir/ruleset/schemas/$schema.json" "$engine_dir/store/schema/$schema/0"
    done
}

main() {
    if [ $# -lt 2 ]; then
        echo "Usage: $0 <github_working_directory> [<engine_source_directory>] <test_type>"
        exit 1
    fi
    GITHUB_WORKING_DIRECTORY="$1"
    ENGINE_SRC_DIR="$GITHUB_WORKING_DIRECTORY/src/engine"
    TEST_TYPE="$2"  # Third argument is the test type

    ENVIRONMENT_DIR="$GITHUB_WORKING_DIRECTORY/environment"
    ENGINE_DIR="$ENVIRONMENT_DIR/engine"
    setup_directories "$ENVIRONMENT_DIR" "$ENGINE_SRC_DIR" "$TEST_TYPE"
    setup_engine "$ENGINE_SRC_DIR" "$ENGINE_DIR"

    if [ "$TEST_TYPE" = "health_test" ]; then
        load_integrations_policies "$ENVIRONMENT_DIR" "$ENGINE_SRC_DIR" "$ENGINE_DIR"
    fi
}
main "$@"
