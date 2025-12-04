#!/bin/bash

dataTrain="/pnfs/iihe/cms/store/user/kskovpen/PNet_LeptonID/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8/TTtoLNu2Q_TuneCP5_13p6TeV_powheg-pythia8_Run3Winter24_NanoAODv15_PNet_LeptonID_20251202/251202_211715/0000/tree*.root"

~/.local/bin/weaver --data-train ${dataTrain} \
 --data-test ${dataTrain} \
 --data-config lepmva/muon_binary.txt \
 --network-config networks/particlenet_pf_sv_withhighlevel.py \
 --model-prefix model \
 --gpus "" --batch-size 512 --start-lr 5e-3 --num-epochs 20 --optimizer ranger \
 --log logs/train.log

#~/.local/bin/weaver --data-train ${dataTrain} \
# --data-test ${dataTrain} \
# --data-config lepmva/muon_binary.txt \
# --network-config networks/particlenet_pf_sv_withhighlevel.py \
# --model-prefix model \
# --gpus 0,1,2,3 --batch-size 512 --start-lr 5e-3 --num-epochs 20 --optimizer ranger \
# --log logs/train.log
