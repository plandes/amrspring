#!/bin/bash

export PYTHONPATH=$PYTHONPATH:.

mkdir -p /opt/data/cache

python bin/inference_server.py \
    --checkpoint /opt/models/model.pt \
    --beam-size 5 \
    --batch-size 500 \
    --penman-linearization \
    --use-pointer-tokens \
    > /opt/data/server.log 2>&1
