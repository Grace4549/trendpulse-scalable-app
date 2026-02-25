
from flask import Flask, jsonify, request
import time

app = Flask(__name__)

@app.route("/")
def home():
    return "Welcome to TrendPulse 🚀"

@app.route("/dashboard")
def dashboard():
    time.sleep(2)
    return "Dashboard Data Loaded"

@app.route("/api/data")
def api_data():
    return jsonify({"users": 1200, "active": 876})

@app.route("/upload", methods=["POST"])
def upload():
    file = request.files.get("file")
    if not file:
        return "No file uploaded", 400
    return "File uploaded successfully"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
