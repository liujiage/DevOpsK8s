display_usage() {
        echo -e "\nUsage:\n./show_status.sh hosts_file \n"
        }


# if less than two arguments supplied, display usage
        if [  $# -lt 1 ]
        then
                display_usage
                exit 1
        fi

# check whether user had supplied -h or --help . If yes display usage
        if [[ ( $* == "--help") ||  $* == "-h" ]]
        then
                display_usage
                exit 0
        fi

# display usage if the script is not run as root user
        if [[ $USER == "root" ]]; then
                echo "This script must not be run as root!"
                exit 1
        fi

# shellcheck disable=SC2068
for hs in $@
do
        echo -e "\033[47;35m $hs: \033[0m"
        ansible-playbook -i $hs show_status.yml
done