#!/bin/bash

dataTrain="${VSC_DATA}/tree*.root"

${VSC_SCRATCH}/pip/bin/weaver --data-train ${dataTrain} \
 --data-test ${dataTrain} \
 --data-config lepmva/muon_binary.txt \
 --network-config networks/particlenet_pf_sv_withhighlevel.py \
 --model-prefix model \
 --gpus 0,1,2,3 --batch-size 512 --start-lr 5e-3 --num-epochs 20 --optimizer ranger \
 --log logs/train.log

#~/.local/bin/weaver --data-train ${dataTrain} \
# --data-test ${dataTrain} \
# --data-config lepmva/muon_binary.txt \
# --network-config networks/particlenet_pf_sv_withhighlevel.py \
# --model-prefix model \
# --gpus "" --batch-size 512 --start-lr 5e-3 --num-epochs 20 --optimizer ranger \
# --log logs/train.log
