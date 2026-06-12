from flask import Flask, jsonify
import os
import socket

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "project": "Python DevOps Dashboard",
        "message": "Running successfully"
    })

@app.route('/health')
def health():
    return jsonify({"status": "UP"})

@app.route('/info')
def info():
    return jsonify({
        "environment": os.getenv("ENVIRONMENT", "local"),
        "hostname": socket.gethostname()
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
