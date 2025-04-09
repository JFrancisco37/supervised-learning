
# UFRGS – Artificial Intelligence Assignment 1

**Course**: Artificial Intelligence (INF01048)  
**Institution**: Federal University of Rio Grande do Sul (UFRGS)  
**Professor**: Joel Luís Carbonera  
**Department**: Applied Informatics, Institute of Informatics  

## 🧑‍💻 Group Members

- João Francisco Hirtenkauf Munhoz – 00275634
- Nome - Cartao
- Nome - Cartao

---

## 📍 Assignment Overview

This assignment is divided into two main parts:

### 1. Linear Regression (from scratch)

Implementation of linear regression using gradient descent to predict farm prices in Alegrete based on land area. The dataset is fictional and contains two columns: land area (hectares) and price (thousands of BRL).

**Files**:
- `alegrete.py`: contains the implementation of `compute_mse`, `step_gradient`, and `fit`.
- `alegrete.ipynb`: used to load and visualize the dataset and the training process.

**Best parameters**:
- Initial values:  
  `b = ...`  
  `w = ...`  
- Learning rate (`alpha`): `...`  
- Number of iterations: `...`  
- Final MSE: `...`

---

### 2. Neural Networks with TensorFlow/Keras

Experiments using convolutional neural networks (CNNs) for image classification on the following datasets:

- MNIST
- Fashion MNIST
- CIFAR-10
- CIFAR-100

**File**: `Trabalho_redes_neurais.ipynb`  
Includes the best configurations tested for each dataset.

---

## 🧪 Dataset Summary

| Dataset        | # Classes | # Samples | Image Size            |
|----------------|-----------|-----------|------------------------|
| MNIST          | 10        | 70,000    | 28 × 28 × 1 (grayscale)|
| Fashion MNIST  | 10        | 70,000    | 28 × 28 × 1 (grayscale)|
| CIFAR-10       | 10        | 60,000    | 32 × 32 × 3 (RGB)      |
| CIFAR-100      | 100       | 60,000    | 32 × 32 × 3 (RGB)      |

---

## 📈 Experimental Results

For each dataset, we tested at least 5 different configurations. Below we summarize our reflections and best results.

### Dataset Complexity Ranking (from easiest to hardest)

1. MNIST – simple grayscale digits, low intra-class variation.  
2. Fashion MNIST – slightly more complex due to shape similarity.  
3. CIFAR-10 – color images with more visual complexity.  
4. CIFAR-100 – high number of classes and small image size makes classification harder.

### Best Accuracies and Observations

- **MNIST**: XX% – Improved with 2 dense layers and ReLU activation.  
- **Fashion MNIST**: XX% – Batch normalization helped.  
- **CIFAR-10**: XX% – Convolutional layers improved performance.  
- **CIFAR-100**: XX% – Performance improved with dropout and deeper CNNs.

---

## 🛠️ Extra Techniques Used

- Feature normalization in linear regression  
- Dropout in CNNs  
- Batch normalization  
- Learning rate scheduling (optional)  

---

## ⚙️ Requirements

- Python 3.12  
- Libraries: `numpy`, `pandas`, `tensorflow==2.18`, `numba`  
- Other libraries (if any):  
  - `...`

---

## 📦 Files Submitted

- `alegrete.py`
- `alegrete.ipynb`
- `alegrete.csv`
- `Trabalho_redes_neurais.ipynb`
- `README.md`
- Any additional source code (if applicable)

---

## 📚 Acknowledgments

Artificial Intelligence – INF01048  
Federal University of Rio Grande do Sul (UFRGS)  
Professor Joel Luís Carbonera
