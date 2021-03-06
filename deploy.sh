#!/bin/bash

if [ -d ci_test ]; then
	echo "change workdir"
	cd ci_test
	echo "Pulling from git"
	git pull
else
	echo "Pulling from git"
	git clone https://github.com/rohit-dimagi/ci_test/
	echo "change workdir"
	cd ci_test
fi

echo "Install requirements"
pip install -r requirements.txt

echo "setting env vars"
export ENVIRONMENT=$1
export DATABASE_URI="$2"

echo "running db migration"
python manage.py db upgrade

echo "killing old process"
pkill -f run.py

echo "start application"
nohup python -u run.py </dev/null &>command.log &
