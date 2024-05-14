#!/bin/bash

# Check if the port number is provided, if not, set it to 8000
port=${1:-8000}

docker run -it -v ./:/dev_challenge -w /dev_challenge -p $port:$port python:3.9 python3 app.py start --port $port