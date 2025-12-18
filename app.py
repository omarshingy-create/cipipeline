from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello! This is a simple Flask app running inside Docker. last practical >>> 18 - Dec - 2025"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
