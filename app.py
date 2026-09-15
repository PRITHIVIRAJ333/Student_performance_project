from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/predictor")
def predictor():
    return render_template("predictor.html")


@app.route("/predict", methods=["POST"])
def predict():

    student_name = request.form["student_name"]

    study_hours = float(request.form["study_hours"])
    attendance = float(request.form["attendance"])
    previous_marks = float(request.form["previous_marks"])
    internal_marks = float(request.form["internal_marks"])
    assignment_score = float(request.form["assignment_score"])
    sleep_hours = float(request.form["sleep_hours"])
    extracurricular = int(request.form["extracurricular"])

    # Prediction
    prediction = model.predict([[
        study_hours,
        attendance,
        previous_marks,
        internal_marks,
        assignment_score,
        sleep_hours,
        extracurricular
    ]])[0]

    prediction = round(prediction, 2)

    # Performance category
    if prediction >= 90:
        performance = "Excellent"
        emoji = "🏆"
    elif prediction >= 75:
        performance = "Good"
        emoji = "🌟"
    elif prediction >= 50:
        performance = "Average"
        emoji = "📚"
    else:
        performance = "Needs Improvement"
        emoji = "💪"

    # Recommendations
    recommendations = []

    if study_hours < 4:
        recommendations.append("Increase your daily study hours.")

    if attendance < 75:
        recommendations.append("Try to maintain attendance above 75%.")

    if previous_marks < 50:
        recommendations.append("Focus more on understanding previous topics.")

    if internal_marks < 50:
        recommendations.append("Improve your internal examination preparation.")

    if assignment_score < 50:
        recommendations.append("Complete assignments regularly.")

    if sleep_hours < 6:
        recommendations.append("Maintain at least 6 hours of proper sleep.")

    if not recommendations:
        recommendations.append(
            "Great job! Maintain your current study routine."
        )

    return render_template(
        "result.html",
        name=student_name,
        prediction=prediction,
        performance=performance,
        emoji=emoji,
        recommendations=recommendations
    )


if __name__ == "__main__":
    app.run(debug=True)