#!/bin/bash

export PYTHONPATH=$PYTHONPATH:.

mkdir -p /opt/data/cache

python bin/inference_server.py \
    --checkpoint /opt/models/model.pt \
    --datadir /opt/data \
    --beam-size 5 \
    --max-tokens 200 \
    --batch-size 500 \
    --penman-linearization \
    --use-pointer-tokens \
    > /opt/data/server.log 2>&1
