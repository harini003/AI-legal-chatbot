from flask import Flask, render_template, request, jsonify
import requests

app = Flask(__name__)

RASA_API_URL = "http://localhost:5005/webhooks/rest/webhook"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json["message"]
    response = requests.post(RASA_API_URL, json={"message": user_message})
    bot_responses = [resp["text"] for resp in response.json() if "text" in resp]
    return jsonify({"response": bot_responses})

if __name__ == "__main__":
    app.run(debug=True)
