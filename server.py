"""
Flask server for the Emotion Detection web application.

"""

from flask import Flask, render_template, request
from Emotion_Detection import emotion_detector

app = Flask(__name__)

@app.route("/")
def home():
    """
    Render the main application page.
    """
    return render_template("index.html")

@app.route("/emotionDetector", methods=["GET", "POST"])

def emotion_ddetector():
    """
    Process text input and return formatted emotion analysis.

    Returns:
        str: Formatted emotion analysis or error message.
    """
    text_to_analyze = request.args.get("textToAnalyze")
    if text_to_analyze is None:
        text_to_analyze = request.form.get("textToAnalyze")

    result = emotion_detector(text_to_analyze)

    if result["dominant_emotion"] is None:
        return "Invalid text! Please try again!"

    anger = result["anger"]
    disgust = result["disgust"]
    fear = result["fear"]
    joy = result["joy"]
    sadness = result["sadness"]
    dominant = result["dominant_emotion"]

    return (
        "For the given statement, the system response is "
        f"'anger': {anger}, 'disgust': {disgust}, 'fear': {fear}, "
        f"'joy': {joy} and 'sadness': {sadness}. "
        f"The dominant emotion is {dominant}."
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
