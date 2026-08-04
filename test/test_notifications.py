import unittest

from backend.app import app


class TestNotifications(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_send_notification(self):

        response = self.client.post(
            "/notify",
            json={
                "email": "student@gmail.com"
            }
        )

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()