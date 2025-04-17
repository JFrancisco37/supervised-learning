
# UFRGS – Artificial Intelligence Assignment 1

**Course**: Artificial Intelligence (INF01048)  
**Institution**: Federal University of Rio Grande do Sul (UFRGS)  
**Professor**: Joel Luís Carbonera  
**Department**: Applied Informatics, Institute of Informatics  

## 🧑‍💻 Group Members

- João Francisco Hirtenkauf Munhoz – 00275634
- Luís Antônio Mikhail Dawa - 00313853
- Mario Augusto Brum da Silveira - 00322868

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
  `b = 0`  
  `w = 0`  
- Learning rate (`alpha`): `0.01`  
- Number of iterations: `100`  
- Final MSE: `9.627438022234974`

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

1. MNIST – simple grayscale digits, low intra-class variation. We were able to get good accuracy in the first try with a simple MLP. 
2. Fashion MNIST – slightly more complex due to shape similarity, but we were still able to get a good accuracy in the first try with a simple MLP.
3. CIFAR-10 – color images with more visual complexity. Using a CNN made the accuracy go up
4. CIFAR-100 – high number of classes and more complex object variations makes classification harder. Just using a CNN was not enugh. We had to add multiple layers with more complex functions for the accuracy to go above 50%.

### Best Accuracies and Observations

**MNIST**: Accuracy 94.97%; Time 85.05s;
The network has 3 layers:
- Flatten Layer: Converts the 2D 28×28 pixel image into a 1D vector of 784 elements (28 × 28 = 784).
- Dense Layer 1: A fully connected layer with 128 neurons and ReLU activation, which helps the network learn non-linear patterns.
- Dense Layer 2: A fully connected layer with 10 neurons, one for each digit class (0–9) and Softmax activation, which turns the outputs into probabilities that sum to 1.  

**Fashion MNIST**: Accuracy 83.04%; Time 96.50s;
We used the same configuration as before and it worked well enough
The network has 3 layers:
- Flatten Layer: Converts the 2D 28×28 pixel image into a 1D vector of 784 elements (28 × 28 = 784).
- Dense Layer 1: A fully connected layer with 128 neurons and ReLU activation, which helps the network learn non-linear patterns.
- Dense Layer 2: A fully connected layer with 10 neurons, one for each digit class (0–9) and Softmax activation, which turns the outputs into probabilities that sum to 1.  


**CIFAR-10**: Accuracy 56.66%; Time 402.34s  
Convolutional layers improved performance significantly compared to dense-only models.  
The network has 5 layers:
- **Conv2D Layer 1**: 32 filters of size 3×3 with ReLU activation, extracts local features from the 32×32 RGB images.
- **MaxPooling2D**: Downsamples feature maps, reducing dimensionality and helping with translation invariance.
- **Flatten Layer**: Converts the pooled feature maps into a 1D vector.
- **Dense Layer 1**: A fully connected layer with 64 neurons and ReLU activation.
- **Dense Layer 2**: A fully connected layer with 10 neurons and Softmax activation for classification.

---

**CIFAR-100**: Accuracy 51.13%; Time 10212.84s  
Performance improved with dropout, batch normalization, and a deeper CNN architecture.  
The network has multiple convolutional blocks followed by fully connected layers:
- **Conv2D Block 1**: Two 64-filter convolutional layers (3×3, 'same' padding) with ReLU and batch normalization.
- **MaxPooling2D**: Reduces spatial dimensions; followed by a Dropout (0.25) to reduce overfitting.
- **Conv2D Block 2**: Two 128-filter convolutional layers (3×3, 'same' padding) with ReLU and batch normalization.
- **MaxPooling2D**: Another downsampling layer; followed by Dropout (0.25).
- **Flatten Layer**: Converts the feature maps into a flat vector.
- **Dense Layer 1**: A fully connected layer with 512 neurons, ReLU, batch normalization, and Dropout (0.5).
- **Dense Layer 2**: Final output layer with 100 neurons and Softmax activation for classification across 100 classes.
---


## 🛠️ Extra Techniques Used

- **Feature normalization** (in linear regression task)
- **Dropout**: Helps prevent overfitting in deeper CNNs by randomly deactivating neurons during training.
- **Batch Normalization**: Stabilizes and accelerates training by normalizing layer inputs.

---


## ⚙️ Requirements

- **Python** 3.12  
- **Libraries**:
  - `tensorflow==2.18.0`
  - `matplotlib`


---

## 📦 Files Submitted

- `alegrete.py`
- `alegrete.ipynb`
- `alegrete.csv`
- `Trabalho_redes_neurais.ipynb`
- `README.md`

---

## 📚 Acknowledgments

Artificial Intelligence – INF01048  
Federal University of Rio Grande do Sul (UFRGS)  
Professor Joel Luís Carbonera
