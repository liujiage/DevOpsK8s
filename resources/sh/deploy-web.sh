#! /bin/bash
:<<!
$1 server name you want to deploy (eg:tiny)
$2 version package's version by jenkis (eg:100)
$3 resource code branch by gitlab (eg:dp)
$4 ip address you want to deploy (eg:192.168.1.0)
$5 enable testing (0 disable 1 enable)
$6 deploy history file name (eg:20210910094820-test-reward-33333)

For example:
./deploy-web.sh account 397 dp 10.30.0.48,10.30.0.49 1 20210910094820-test-reward-33333
!
cd /home/mozat/ansible
( dpkg -l |grep expect-dev >/dev/null ) || sudo apt-get -y install expect-dev
[ ! -d "history" ] && mkdir history
time=$(date +%Y%m%d%H%M%S)
dir_name=`cd $(dirname $0) &&pwd`"/"
service_name=$1
version=$(echo $2 |grep -Eo '[0-9]+')
log=$6
[ -z $6 ] && log=$time"-"$service_name"-"$version
#dp means will be get the code resource from pre-releaes branch.
git_version=$3
[ -z $3 ] && git_version='dp'
#add test parameter for testing.
#print the command do not really execute the command.
test=$5
[ -z $5 ] && test=0

echo "$service_name is going to be deployed by version $version on config $git_version deploy ip $4 enable test $test"
#if has service's hosts config then will be begin to process task that deploy the services.
if ( ls $dir_name"hosts/" |grep $1 >/dev/null ); then
    # if ips is null then deploy all servers from hosts
    if [ -z $4 ]; then
        # shellcheck disable=SC1068
        test=0 #all deploy without testing
        cmd="ansible-playbook -i ${dir_name}hosts/${service_name}.hosts --extra-vars \"version=$version service=$service_name git_version=$git_version\" ${dir_name}deploy.yml"
    else
        cmd="ansible-playbook -i ${dir_name}hosts/${service_name}.hosts -l $4 --extra-vars \"version=$version service=$service_name git_version=$git_version\" ${dir_name}deploy.yml"
    fi
    echo -e "executing command $cmd "
    #when ips is not null, can enable testing
    if (( test == 0 )); then
        bash -c "unbuffer $cmd" |tee history/$log
        aws s3 cp history/$log  s3://loops-ansible-history/dp/
        find history/ -type f -mtime +100 |xargs -r -n1 rm
    fi
fi