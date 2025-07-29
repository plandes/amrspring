#!/bin/bash

export PYTHONPATH=$PYTHONPATH:.
export TRANSFORMERS_OFFLINE=1
BASE_DIR=${BASE_DIR:-/opt}
mkdir -p ${BASE_DIR:-/opt}/data

python bin/inference_server.py \
    --checkpoint ${BASE_DIR:-/opt}/models/model.pt \
    --datadir ${BASE_DIR:-/opt}/data \
    --beam-size 5 \
    --max-tokens 200 \
    --batch-size 500 \
    --penman-linearization \
    --use-pointer-tokens \
    > ${BASE_DIR:-/opt}/data/server.log 2>&1
