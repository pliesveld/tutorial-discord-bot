#!/bin/bash

set -euo pipefail

export WORKSPACE='.'

PATH=$WORKSPACE/venv/bin:/usr/local/bin:$PATH
if [ ! -d "venv" ]; then
	pip3 install virtualenv
	python3 -m virtualenv venv
fi
. venv/bin/activate
pip3 install -r requirements.txt


set -x
python3 "bot.py"

