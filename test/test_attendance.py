import unittest

from backend.app import app


class TestAttendance(unittest.TestCase):

    def setUp(self):
        self.client = app.test_client()

    def test_mark_attendance(self):

        response = self.client.post(
            "/attendance",
            json={
                "student_id": 1,
                "event_id": 1,
                "status": "Present"
            }
        )

        self.assertEqual(response.status_code, 200)

    def test_get_attendance(self):

        response = self.client.get("/attendance")

        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest.main()