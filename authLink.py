from flask import Flask, request
app = Flask(__name__)

@app.route("/signup", methods=["POST"])
def signup():
    username = request.form["username"]
    email = request.form["email"]
    password = request.form["password"]
    sign_up(username, email, password)
    return "Sign up successful!"

@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    password = request.form["password"]
    user = log_in(email, password)
    if user:
        return "Login successful!"
    else:
        return "Login failed."

if __name__ == "__main__":
    app.run(debug=True)