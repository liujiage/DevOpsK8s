#! /bin/bash

n=$1
[ -z $1 ] && n=10

for ((i=0; i<n; i++))
do
    echo "starting ...."
    echo "writing records into deploy.log "
    echo "deploy tiny service at date $(date)"  >> deploy.log
    echo "writing done"
    echo "end"
done