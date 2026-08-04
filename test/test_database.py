import unittest

from backend.database import get_connection


class TestDatabase(unittest.TestCase):

    def test_connection(self):

        connection = get_connection()

        self.assertIsNotNone(connection)

        connection.close()


if __name__ == "__main__":
    unittest.main()