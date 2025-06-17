from flask import Flask, request, jsonify
from transformers import pipeline

app = Flask(__name__)
chatbot = pipeline("text-generation", model="EleutherAI/gpt-neo-1.3B")

@app.route("/")
def home():
    return "HumJaisa AI is Running ✅"

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    if not user_input:
        return jsonify({"error": "No input"}), 400

    response = chatbot(user_input, max_length=100, do_sample=True)[0]["generated_text"]
    return jsonify({"reply": response})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
