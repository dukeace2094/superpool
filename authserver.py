import psycopg2
import hashlib
from flask import Flask, request, jsonify
app = Flask(__name__)

# Connect to the database
conn = psycopg2.connect(
  host="localhost",
  database="superpool_db",
  user="jp",
  password=""
)
cursor = conn.cursor()

# Function to hash a password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Function to check if a password is correct
def check_password(email, password):
    cursor.execute("SELECT password FROM users WHERE email=%s", (email,))
    hashed_password = cursor.fetchone()[0]
    return hashed_password == hash_password(password)

# Function to sign up a user
@app.route("/signup", methods=["POST"])
def signup():
    request_data = request.get_json()
    email = request_data['email']
    username = request_data['username']
    password = request_data['password']

    # Check if user already exists in database
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user is not None:
        return jsonify({"success": False, "message": "Email already exists"})

    # Hash password
    hashed_password = hash_password(password)

    # Add user to database
    cursor.execute("INSERT INTO users (email, username, password) VALUES (%s, %s, %s)", (email, username, hashed_password))
    conn.commit()

    # Sign up successful
    return jsonify({"success": True, "message": "Sign up successful"})

# Function to log in a user

@app.route("/login", methods=["POST"])
def login():
    request_data = request.get_json()
    email = request_data['email']
    password = request_data['password']

    # Check if user exists in database
    cursor.execute("SELECT * FROM users WHERE email=%s", (email,))
    user = cursor.fetchone()
    if user is None:
        return jsonify({"success": False, "message": "Email not found"})

    # Verify password
    if not check_password(password, user[3]):
        return jsonify({"success": False, "message": "Incorrect password"})

    # Login successful
    return jsonify({"success": True, "message": "Login successful", "username": user[1]})
