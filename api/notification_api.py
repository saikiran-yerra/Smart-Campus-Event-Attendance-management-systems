from flask import Blueprint, request, jsonify

notification_api = Blueprint("notification_api", **name**)

@notification_api.route("/api/notify", methods=["POST"])
def send_notification():

```
data = request.get_json()

return jsonify({
    "message": "Notification sent successfully",
    "email": data["email"]
})
```
