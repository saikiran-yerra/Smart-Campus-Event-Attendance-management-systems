import unittest

from backend.app import app


class TestEvents(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_create_event(self):

        response = self.client.post(
            "/events",
            json={
                "event_name": "Tech Fest",
                "event_date": "2026-08-10",
                "location": "Auditorium"
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_get_events(self):

        response = self.client.get("/events")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()