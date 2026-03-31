# 📊 Data Mining Assignment

This repository contains implementations of basic Data Mining algorithms using Python and Machine Learning.

---

## 📁 Folder Structure

```
DataMining/
│
├── .gitignore
├── README.md
│
├── digit_recognition/
│   ├── main.py
│   └── mnist_train.csv
│
├── naive_bayes/
│   └── main.py
│
├── knn_iris/
│   └── main.py
```

---

## 📥 Dataset

MNIST dataset is too large to upload on GitHub.

Download it from:
https://www.kaggle.com/datasets/oddrationale/mnist-in-csv

After downloading, place:
mnist_train.csv inside the `digit_recognition` folder.

---

## 🧠 Implemented Algorithms

### 1️⃣ Digit Recognition using Logistic Regression

* Dataset: MNIST (CSV format)
* Description: Classifies handwritten digits (0–9)
* Accuracy: ~90–94%

---

### 2️⃣ Naive Bayes Classification

* Dataset: MNIST (Online via OpenML)
* Algorithm: Gaussian Naive Bayes
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
