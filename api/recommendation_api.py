from flask import Blueprint, jsonify

recommendation_api = Blueprint(
"recommendation_api",
**name**
)

@recommendation_api.route(
"/api/recommendations/[int:student_id](int:student_id)",
methods=["GET"]
)
def get_recommendations(student_id):

```
recommendations = [

    "AI Workshop",

    "Hackathon",

    "Tech Fest"

]

return jsonify({

    "student_id": student_id,

    "recommended_events": recommendations

})
```
