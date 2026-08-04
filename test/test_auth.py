import unittest

from backend.app import app

class TestAuthentication(unittest.TestCase):

```
def setUp(self):

    self.client = app.test_client()

    self.client.testing = True


def test_login_success(self):

    response = self.client.post(

        "/login",

        json={

            "email": "admin@gmail.com",

            "password": "admin"

        }

    )

    self.assertEqual(response.status_code, 200)


def test_login_failure(self):

    response = self.client.post(

        "/login",

        json={

            "email": "user@gmail.com",

            "password": "wrong"

        }

    )

    self.assertEqual(response.status_code, 401)
```

if **name** == "**main**":

```
unittest.main()
```
