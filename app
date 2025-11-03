from flask import Flask, request
app = Flask(__name__)

@app.route("/")
def index():
    return "Cloudflare demo app is running!"

@app.route("/login", methods=["POST"])
def login():
    user = request.form.get("user")
    pw = request.form.get("pass")
    if user == "admin" and pw == "secret":
        return "auth ok"
    return "bad", 401

@app.route("/api")
def api():
    return {"message": "API is alive"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
