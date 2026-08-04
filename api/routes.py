from auth_api import auth_api
from events_api import events_api
from attendance_api import attendance_api
from notification_api import notification_api
from recommendation_api import recommendation_api

def register_routes(app):

```
app.register_blueprint(auth_api)

app.register_blueprint(events_api)

app.register_blueprint(attendance_api)

app.register_blueprint(notification_api)

app.register_blueprint(recommendation_api)
```
