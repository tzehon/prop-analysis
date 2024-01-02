#!/bin/bash

source ./env.dev.sh

docker run -p 9090:$PORT  \
    -e PORT=$PORT \
    -e ACCESS_KEY=$ACCESS_KEY \
    -e ATLAS_CONNECTION_STRING=$ATLAS_CONNECTION_STRING \
    $URL