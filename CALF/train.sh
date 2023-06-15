#!/bin/sh

python src/main.py --SoccerNet_path=/path_to_soccer \
--features=CLIP_feats.npz \
--num_features=1024 \
--model_name=CALF_clip_full_data \
--batch_size 32 \
--evaluation_frequency 20 \
--chunks_per_epoch 18000 \
