import json
import random
import nltk
import numpy as np
from flask import Flask, request, jsonify
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import LogisticRegression
import warnings
warnings.filterwarnings("ignore")

# Download required NLTK data
nltk.download('punkt')

# Load and preprocess data
with open("business_chatbot_data.json", "r") as f:
    data = json.load(f)

patterns = []
tags = []
responses = {}

for intent in data["intents"]:
    for pattern in intent["patterns"]:
        patterns.append(pattern)
        tags.append(intent["tag"])
    responses[intent["tag"]] = intent["responses"]

# Vectorize patterns and train model
vectorizer = TfidfVectorizer(tokenizer=nltk.word_tokenize)
X = vectorizer.fit_transform(patterns)
y = np.array(tags)

model = LogisticRegression()
model.fit(X, y)

# Create Flask app
app = Flask(__name__)

@app.route("/")
def index():
    return "Chatbot API is running!"

@app.route("/chat", methods=["GET", "POST"])
def chat():
    if request.method == "POST":
        data = request.get_json()
        user_input = data.get("message") if data else None
    else:  # GET
        user_input = request.args.get("message")

    if not user_input:
        return jsonify({"error": "No input provided."}), 400

    input_vec = vectorizer.transform([user_input])
    pred_tag = model.predict(input_vec)[0]
    response = random.choice(responses[pred_tag])

    return jsonify({"response": response})

if __name__ == "__main__":
    app.run(debug=True)
