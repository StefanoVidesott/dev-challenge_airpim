#!/bin/bash

#check if direcotry does not exist
if [ ! -d "/tmp/dev-challenge_venv" ]; then
    echo "Creating virtual environment"
    mkdir /tmp/dev-challenge_venv
    python3 -m venv /tmp/dev-challenge_venv
    source /tmp/dev-challenge_venv/bin/activate
    pip install -r requirements.txt
else
    echo "Virtual environment already exists"
    source /tmp/dev-challenge_venv/bin/activate
fi

python3 app.py