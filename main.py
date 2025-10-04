import os
import numpy as np
import matplotlib.pyplot as plt
from src.data_loader import load_images_recursively, normalize_data
from src.pca_model import PCAFromScratch

# ==========================================================
# CONFIGURATION
# ==========================================================
RAW_DATA_DIR = "data/raw/lfw_subset/lfw_home/lfw_funneled"
IMAGE_SIZE = (100, 100)
N_COMPONENTS = 20
MAX_PEOPLE = 60          # limit to keep it fast
MAX_IMAGES_PER_PERSON = 3

# ==========================================================
# ENSURE RESULT FOLDERS EXIST
# ==========================================================
os.makedirs("results/eigenfaces", exist_ok=True)
os.makedirs("results/reconstructions", exist_ok=True)

# ==========================================================
# LOAD DATA
# ==========================================================
X, img_shape, labels = load_images_recursively(
    RAW_DATA_DIR,
    image_size=IMAGE_SIZE,
    max_people=MAX_PEOPLE,
    max_images_per_person=MAX_IMAGES_PER_PERSON
)
print(f"Loaded {X.shape[0]} human face images of size {img_shape}")

# ==========================================================
# NORMALIZE & PCA
# ==========================================================
X_centered, mean_face = normalize_data(X)
pca = PCAFromScratch(n_components=N_COMPONENTS)
pca.fit(X_centered)
print("Explained variance ratios:", pca.explained_variance_ratio_)

# ==========================================================
# SAVE MEAN FACE
# ==========================================================
mean_face_img = mean_face.reshape(img_shape)
plt.imshow(mean_face_img, cmap='gray')
plt.title("Mean Face")
plt.axis('off')
mean_path = "results/mean_face.png"
plt.savefig(mean_path, bbox_inches='tight')
plt.close()
print(f"✅ Saved {mean_path}")

# ==========================================================
# SAVE EIGENFACES
# ==========================================================
for i in range(N_COMPONENTS):
    eigenface = pca.components_[i].reshape(img_shape)
    plt.imshow(eigenface, cmap='gray')
    plt.title(f"Eigenface {i+1}")
    plt.axis('off')
    out_path = f"results/eigenfaces/eigenface_{i+1}.png"
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved {out_path}")

# ==========================================================
# FACE RECONSTRUCTION DEMO
# ==========================================================
sample_idx = 0  # choose any sample
original = X[sample_idx].reshape(img_shape)

for k in [5, 10, 20]:
    pca_k = PCAFromScratch(n_components=k)
    pca_k.fit(X_centered)
    X_proj = pca_k.transform(X_centered)
    reconstruction = pca_k.inverse_transform(X_proj[sample_idx])

    plt.imshow(reconstruction.reshape(img_shape), cmap='gray')
    plt.title(f"Reconstructed with {k} Eigenfaces")
    plt.axis('off')
    out_path = f"results/reconstructions/reconstruction_{k}.png"
    plt.savefig(out_path, bbox_inches='tight')
    plt.close()
    print(f"✅ Saved {out_path}")

print("🎉 All images saved in the 'results/' folder.")

