#!/bin/bash

source ./env.dev.sh

docker build . --tag $URL --platform linux/amd64