import pandas as pd
import pickle

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error


# =====================================
# LOAD DATASET
# =====================================

df = pd.read_csv("dataset.csv")

print()
print("===================================")
print(" STUDENT PERFORMANCE PREDICTOR")
print("===================================")

print("Dataset loaded successfully!")
print("Total records:", len(df))


# =====================================
# INPUT FEATURES
# =====================================

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


# =====================================
# TARGET
# =====================================

y = df["final_score"]


# =====================================
# TRAIN TEST SPLIT
# =====================================

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# =====================================
# RANDOM FOREST MODEL
# =====================================

model = RandomForestRegressor(
    n_estimators=300,
    random_state=42,
    max_depth=12
)


# =====================================
# TRAIN
# =====================================

print()
print("Training model...")

model.fit(X_train, y_train)

print("Model trained successfully!")


# =====================================
# TEST
# =====================================

predictions = model.predict(X_test)

error = mean_absolute_error(
    y_test,
    predictions
)

print(
    "Mean Absolute Error:",
    round(error, 2)
)


# =====================================
# SAVE MODEL
# =====================================

with open("model.pkl", "wb") as file:

    pickle.dump(model, file)


print()
print("model.pkl created successfully!")
print("===================================")
print()