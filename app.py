from flask import Flask, request
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

users = [
    {"id": 1, "email": "beemo@beemo.com", "name": "Beemo", "points": 8},
    {"id": 2, "email": "mainlevel@email.com", "name": "Main Level", "points": 9},
    {"id": 3, "email": "admin@email.com", "name": "Admin", "points": 7},
    {"id": 4, "email": "user@gmail.com", "name": "User", "points": 5}
]


# Get all users
@app.route("/users", methods=["GET"])
def get_users():
    return users


# Get user by email
@app.route("/users", methods=["POST"])
def user_by_email():
    email = request.json["email"]
    for user in users:
        if user['email'] == email:
            return user
    return {"error": "User not found"}


if __name__ == "__main__":
    app.run(debug=True, port=5001)
