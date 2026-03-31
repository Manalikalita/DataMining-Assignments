# 📊 Data Mining Assignment

This repository contains implementations of basic Data Mining algorithms using Python and Machine Learning.

---

## 📁 Folder Structure

```
DataMining/
│
├── digit_recognition/
│   ├── main.py
│   └── mnist_train.csv(Dataset: Download MNIST dataset from Kaggle (https://www.kaggle.com/datasets/            oddrationale/mnist-in-csv) and place mnist_train.csv inside the digit_recognition folder.)
│
├── naive_bayes/
│   └── main.py
│
├── knn_iris/
│   └── main.py
│
└── README.md
```

---

## 🧠 Implemented Algorithms

### 1️⃣ Digit Recognition using Logistic Regression

* Dataset: MNIST (CSV format)
* Description: Classifies handwritten digits (0–9)
* Accuracy: ~90–94%

---

### 2️⃣ Naive Bayes Classification

* Dataset: MNIST (Online via OpenML)
* Algorithm: Multinomial Naive Bayes
* Description: Probabilistic classifier based on Bayes theorem
* Accuracy: ~80–90%

---

### 3️⃣ KNN Classification on Iris Dataset

* Dataset: Iris (built-in)
* Algorithm: K-Nearest Neighbors (K=3)
* Description: Classifies flowers into Setosa, Versicolor, and Virginica
* Accuracy: ~95–100%

---

## ⚙️ Requirements

Install required libraries:

```
pip install numpy pandas matplotlib scikit-learn
```

---

## ▶️ How to Run

### 🔹 Digit Recognition

```
cd digit_recognition
python main.py
```

### 🔹 Naive Bayes

```
cd naive_bayes
python main.py
```

### 🔹 KNN Iris

```
cd knn_iris
python main.py
```

---

## 📌 Key Concepts

* Classification Algorithms
* Logistic Regression
* Naive Bayes
* K-Nearest Neighbors (KNN)
* Data Preprocessing
* Model Evaluation (Accuracy)

---

## 👩‍💻 Author

* Name: Manali Kalita

---
