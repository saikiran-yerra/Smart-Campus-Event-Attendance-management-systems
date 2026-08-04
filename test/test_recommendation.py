import unittest

from ai_recommendation.recommendation_engine import recommend_events


class TestRecommendation(unittest.TestCase):

    def test_recommendation(self):

        student = {
            "technical_interest": 9,
            "sports_interest": 2,
            "cultural_interest": 1
        }

        result = recommend_events(student)

        self.assertIsNotNone(result)


if __name__ == "__main__":
    unittest.main()