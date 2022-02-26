#! /bin/bash
cd /home/ubuntu/DevOps
export FLASK_APP=index
export FLASK_ENV=development
flask run --host=10.30.0.35
