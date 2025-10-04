# 🧠 The Typical Look Within a Group  
### *Statistical Face Modeling Using PCA*

---

## 📘 Overview

This project explores how **linear algebra** and **Principal Component Analysis (PCA)** can be applied to identify and visualize the **typical look within a group of human faces**.  

By leveraging **Singular Value Decomposition (SVD)**, the project constructs:  
- the **mean face** (a statistical average appearance), and  
- a set of **eigenfaces** (the key patterns of variation).  

This allows us to represent, compress, and reconstruct human facial data in a lower-dimensional space — revealing both group-level similarity and individual diversity.

---

## 🎯 Objectives

- Compute the **average face** for a group of aligned facial images.  
- Derive **eigenfaces** — principal components capturing major visual variation.  
- **Reconstruct faces** using a limited number of components.  
- Compare **intra-group** and **inter-group** facial characteristics statistically.  
- Demonstrate how **computational linear algebra** techniques can model complex visual data efficiently.

---

## 🧩 Methodology

1. **Data Loading**  
   - Images are loaded and converted to grayscale.  
   - Each image is flattened into a vector of pixel intensities.  
   - The data matrix \( X \in \mathbb{R}^{n \times d} \) is constructed, where each row represents a face.

2. **Data Centering**  
   - Compute the mean face \( \mu \).  
   - Subtract \( \mu \) from each image to center the data.

3. **PCA via SVD (Compact Trick)**  
   - Compute eigen-decomposition of \( X X^T \).  
   - Derive eigenfaces by mapping eigenvectors back to the original image space.

4. **Reconstruction**  
   - Each face is approximated as a linear combination of the mean face and top-k eigenfaces:
     \[
     X_i \approx \mu + a_1v_1 + a_2v_2 + \dots + a_kv_k
     \]

---

## 🧮 Mathematical Insight

The project demonstrates how **Singular Value Decomposition (SVD)**:
\[
X = U \Sigma V^T
\]
enables efficient dimensionality reduction and data reconstruction in high-dimensional spaces.  

Each eigenface represents a **basis vector** in the “face space”, and each human face becomes a **coordinate point** in that space — an elegant intersection of mathematics, data, and perception.

---

## 🧠 Real-World Applications

- 🧬 **Data Compression** — storing high-dimensional image data with minimal information loss.  
- 🔍 **Face Recognition** — matching identities via PCA projection coefficients.  
- 🧑‍🎨 **Anthropological Visualization** — studying statistical appearance trends *within groups*.  
- 🧮 **Fair AI Research** — understanding and correcting representation bias in face datasets.  

---

## ⚙️ Project Structure

```
eigenfaces_reimagined/
├── src/
│   ├── data_loader.py        # Loads and preprocesses images
│   ├── pca_model.py          # PCA implementation (compact trick)
│   └── visualization.py      # (optional) for plotting/animation
├── data/
│   └── raw/                  # Untracked dataset folder
├── results/
│   ├── eigenfaces/           # Saved eigenface visualizations
│   ├── reconstructions/      # Reconstructed faces
│   └── mean_face.png         # Statistical average face
├── main.py                   # Main execution script
├── requirements.txt          # Dependencies
└── README.md                 # Project description
```

---

## 💻 Running the Project

### 1️⃣ Clone the repository
```bash
git clone https://github.com/BitwodedSeleshiDemissie/The-Typical-Look-Within-a-Group-Statistical-Face-Modeling-Using-PCA.git
cd The-Typical-Look-Within-a-Group-Statistical-Face-Modeling-Using-PCA
```

### 2️⃣ Create a virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3️⃣ Add your dataset
Place your face dataset (e.g., LFW subset) in:
```
data/raw/
```

### 4️⃣ Run the model
```bash
python3 main.py
```

---

## 🖼️ Example Outputs

| Visualization | Description |
|----------------|--------------|
| **Mean Face** | The statistical average of all faces in the dataset. |
| **Eigenfaces** | Principal components capturing key facial variations. |
| **Reconstructions** | Stepwise reconstruction of faces using top-k eigenfaces. |

All outputs are automatically saved in the `results/` folder.

---

## 📚 Theoretical References

- **Gilbert Strang**, *Linear Algebra and Learning from Data* (2019)  
- **Yousef Saad**, *Iterative Methods for Sparse Linear Systems* (2003)  
- **Turk & Pentland (1991)**, *Eigenfaces for Recognition*, Journal of Cognitive Neuroscience  

---

## ⚖️ Ethical Considerations

This project treats facial data purely as **numerical signals** for mathematical exploration.  
It does **not** make or support biological, racial, or cultural claims about facial features.  
All results are **statistical and dataset-dependent**, intended for educational and computational insight only.

---

## ✨ Acknowledgements

Developed as part of the **Computational Linear Algebra for Large Scale Problems** course at **Politecnico di Torino (PoliTo)**.  

Project Author: [**Bitwoded Seleshi Demissie**](https://github.com/BitwodedSeleshiDemissie)  
Instructor: Prof. Andrea Borio  

---

## 🧩 Keywords
`PCA` • `Linear Algebra` • `Eigenfaces` • `Dimensionality Reduction` • `Data Science` • `SVD` • `Face Modeling` • `Computational Mathematics`
