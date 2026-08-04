import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier

import pickle


# Load dataset
dataset = pd.read_csv("dataset.csv")


# Input features
X = dataset[
    [
        "technical_interest",
        "sports_interest",
        "cultural_interest"
    ]
]


# Target output
y = dataset["recommended_event"]


# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Create and train model
model = DecisionTreeClassifier()

model.fit(X_train, y_train)


# Save trained model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)


print("Model trained successfully")