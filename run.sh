#!/bin/bash

source ./env.dev.sh

docker run -p 9090:$PORT -e PORT=$PORT -e ACCESS_KEY=$ACCESS_KEY $URL