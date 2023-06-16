import torch
import clip
import numpy as np
from PIL import Image
from PIL import UnidentifiedImageError

import os
from tqdm import tqdm


path = './PaddleDetection/france_ligue-1/'


device = "cuda" if torch.cuda.is_available() else "cpu"
model, preprocess = clip.load("ViT-B/32", device=device)

for i in tqdm(range(145045, len(os.listdir(path)))):
    tmp = path+os.listdir(path)[i]
    try:
        image = preprocess(Image.open(tmp)).unsqueeze(0).to(device)
    except (UnidentifiedImageError,IsADirectoryError) as error:
        continue
    with torch.no_grad():
        image_features = model.encode_image(image)
    image_features_2 = image_features.cpu().detach().numpy()
    np.save("./clip_features/feat_"+os.listdir(path)[i], image_features_2)