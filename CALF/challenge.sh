#!/bin/sh

python src/main.py --SoccerNet_path=/path_to_data \
--features=CLIP_feats.npz \
--num_features=1024 \
--model_name=CALF_clip_full_data \
--challenge \
--test_only