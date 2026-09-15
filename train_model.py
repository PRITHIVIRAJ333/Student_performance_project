import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

# Load dataset
data = pd.read_csv("dataset.csv")

# Input features
X = data[
    [
        "study_hours",
        "attendance",
        "previous_marks",
        "internal_marks",
        "assignment_score",
        "sleep_hours",
        "extracurricular"
    ]
]

# Target
y = data["final_score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create ML model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")
print("Model saved as model.pkl")

# Check accuracy
score = model.score(X_test, y_test)
print("Model R2 Score:", score)