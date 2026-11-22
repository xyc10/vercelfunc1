from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello World from Flask on Vercel!"

@app.route("/api/hello")
def hello():
    return jsonify({
        "message": "Hello World!",
        "framework": "Flask",
        "platform": "Vercel"
    })
