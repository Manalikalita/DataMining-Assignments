import pandas as pd
import random
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

# Step 1: Load dataset
print("Loading dataset...")
data = pd.read_csv("mnist_train.csv").sample(10000)

# Step 2: Separate features & labels
X = data.drop("label", axis=1).values
y = data["label"].values

# Step 3: Normalize
X = X / 255.0

# Step 4: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 5: Train model
print("Training model...")
model = LogisticRegression(max_iter=1000, solver='saga')
model.fit(X_train, y_train)

# Step 6: Predict
y_pred = model.predict(X_test)

# Step 7: Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy:", accuracy * 100)

# Step 8: Show random result
index = random.randint(0, len(X_test) - 1)

plt.imshow(X_test[index].reshape(28, 28), cmap='gray')
plt.title(f"Predicted: {y_pred[index]}, Actual: {y_test[index]}")
plt.axis('off')
plt.show()