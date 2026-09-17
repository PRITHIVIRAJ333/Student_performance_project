import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error

# Load dataset
df = pd.read_csv("dataset.csv")

print("Dataset loaded successfully!")
print("Total records:", len(df))

# Input features
X = df[
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

# Output
y = df["final_score"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Test model
predictions = model.predict(X_test)

error = mean_absolute_error(y_test, predictions)

print("Model trained successfully!")
print("Mean Absolute Error:", round(error, 2))

# Save model
with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("model.pkl created successfully!")