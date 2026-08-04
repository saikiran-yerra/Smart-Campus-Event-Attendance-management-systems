from flask import Blueprint, request, jsonify

auth_api = Blueprint("auth_api", **name**)

@auth_api.route("/api/register", methods=["POST"])
def register():

```
data = request.get_json()

user = {
    "name": data["name"],
    "email": data["email"],
    "role": data["role"]
}

return jsonify({
    "message": "User registered successfully",
    "user": user
}), 201
```

@auth_api.route("/api/login", methods=["POST"])
def login():

```
data = request.get_json()

email = data["email"]
password = data["password"]

if email == "admin@gmail.com" and password == "admin123":

    return jsonify({
        "message": "Login successful",
        "token": "sample-jwt-token"
    })

return jsonify({
    "message": "Invalid credentials"
}), 401
```
