#!/bin/bash

set -e -x

for image in hfst omorfi omorfi-mss; do
    docker build -m 4g  -t "cscmss/$image" $image
done
