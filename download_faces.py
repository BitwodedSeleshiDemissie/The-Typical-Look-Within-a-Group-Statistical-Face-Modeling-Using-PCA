# download_faces.py
from sklearn.datasets import fetch_lfw_people
import os

def fetch_lfw_subset(save_path="data/raw/lfw_subset", min_faces=20, resize=0.5):
    """
    Downloads a small, ready-to-use subset of the LFW dataset
    directly via scikit-learn.
    """
    os.makedirs(save_path, exist_ok=True)
    dataset = fetch_lfw_people(
        data_home=save_path,
        min_faces_per_person=min_faces,
        resize=resize,
        color=False
    )
    print(f"✅ Downloaded {dataset.data.shape[0]} face images of shape {dataset.images[0].shape}")
    return dataset

if __name__ == "__main__":
    fetch_lfw_subset()

