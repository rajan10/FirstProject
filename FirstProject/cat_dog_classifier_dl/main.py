import tensorflow_dataset as tf

import os
from PIL import Image

DATASETS = "dataset"

#cretae folders

os.makedirs(f"DATASETS/cat", exist_ok=True)
os.makedirs(f"DATASETS/dog", exist_ok=True)

print("Downloading cat and dog datasets...")



