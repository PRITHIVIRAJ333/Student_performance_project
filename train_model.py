import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
import pickle

data = pd.read_csv("dataset.csv")

features = [
    "study_hours",
    "attendance",
    "previous_marks",
    "internal_marks",
    "assignment_score",
    "sleep_hours",
    "extracurricular"
]

X = data[features]
y = data["final_score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train, y_train)

with open("model.pkl", "wb") as file:
    pickle.dump(model, file)

print("Model trained successfully!")

accuracy = model.score(X_test, y_test)

print("Model R2 Score:", accuracy)
print("model.pkl created successfully!")