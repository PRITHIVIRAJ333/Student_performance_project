from flask import Flask, render_template, request
import pickle
import os

app = Flask(
    __name__,
    template_folder="../templates",
    static_folder="../static"
)

# Load trained model
model_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "model.pkl"
)

with open(model_path, "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predictor")
def predictor():
    return render_template("predictor.html")


@app.route("/predict", methods=["POST"])
def predict():

    name = request.form["name"]

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_marks = float(request.form["previous_marks"])
    internal_marks = float(request.form["internal_marks"])
    assignment_score = float(request.form["assignment_score"])
    sleep_hours = float(request.form["sleep_hours"])
    extracurricular = int(request.form["extracurricular"])

    input_data = [[
        study_hours,
        attendance,
        previous_marks,
        internal_marks,
        assignment_score,
        sleep_hours,
        extracurricular
    ]]

    predicted_score = model.predict(input_data)[0]

    # Keep score between 0 and 100
    predicted_score = max(0, min(100, predicted_score))

    # Performance category
    if predicted_score >= 90:
        performance = "Excellent"
        emoji = "🏆"

    elif predicted_score >= 75:
        performance = "Good"
        emoji = "🌟"

    elif predicted_score >= 50:
        performance = "Average"
        emoji = "📚"

    else:
        performance = "Poor"
        emoji = "💪"

    # Recommendations
    recommendations = []

    if study_hours < 4:
        recommendations.append(
            "Increase your daily study hours."
        )

    if attendance < 75:
        recommendations.append(
            "Try to improve your attendance."
        )

    if previous_marks < 50:
        recommendations.append(
            "Focus on improving your previous academic performance."
        )

    if internal_marks < 50:
        recommendations.append(
            "Prepare more for internal examinations."
        )

    if assignment_score < 50:
        recommendations.append(
            "Complete assignments regularly and on time."
        )

    if sleep_hours < 6:
        recommendations.append(
            "Maintain a healthy 6-8 hours of sleep."
        )

    if not recommendations:
        recommendations.append(
            "Excellent! Keep maintaining your current study habits."
        )

    return render_template(
        "result.html",
        name=name,
        score=round(predicted_score, 2),
        performance=performance,
        emoji=emoji,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)