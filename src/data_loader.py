import os
import cv2
import numpy as np
from tqdm import tqdm

def load_images_recursively(base_path, image_size=(100, 100), max_people=None, max_images_per_person=None):
    """
    Loads grayscale images from subdirectories (like LFW structure).
    Each subfolder corresponds to one person.
    """
    images, labels = [], []
    subdirs = sorted([d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))])
    if max_people:
        subdirs = subdirs[:max_people]

    for subdir in tqdm(subdirs, desc="Loading people"):
        folder = os.path.join(base_path, subdir)
        files = [f for f in os.listdir(folder) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
        if max_images_per_person:
            files = files[:max_images_per_person]

        for file in files:
            img_path = os.path.join(folder, file)
            img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
            if img is None:
                continue
            img = cv2.resize(img, image_size)
            images.append(img.flatten())
            labels.append(subdir)

    X = np.array(images, dtype=np.float64)
    return X, image_size, labels

def normalize_data(X):
    """Center data by subtracting the mean face."""
    mean_face = np.mean(X, axis=0)
    X_centered = X - mean_face
    return X_centered, mean_face

