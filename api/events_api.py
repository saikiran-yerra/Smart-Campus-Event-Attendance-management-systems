from flask import Blueprint, request, jsonify

events_api = Blueprint("events_api", **name**)

events = []

@events_api.route("/api/events", methods=["GET"])
def get_events():

```
return jsonify(events)
```

@events_api.route("/api/events", methods=["POST"])
def create_event():

```
data = request.get_json()

event = {
    "event_id": len(events) + 1,
    "event_name": data["event_name"],
    "event_date": data["event_date"],
    "location": data["location"]
}

events.append(event)

return jsonify({
    "message": "Event created successfully",
    "event": event
}), 201
```

@events_api.route("/api/events/[int:event_id](int:event_id)", methods=["DELETE"])
def delete_event(event_id):

```
return jsonify({
    "message": f"Event {event_id} deleted"
})
```
