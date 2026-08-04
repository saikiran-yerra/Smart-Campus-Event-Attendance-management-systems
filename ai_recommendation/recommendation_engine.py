import pandas as pd
import pickle
import os


BASE_DIR = os.path.dirname(os.path.abspath(__file__))


with open(os.path.join(BASE_DIR, "model.pkl"), "rb") as file:
    model = pickle.load(file)


def recommend_events(student_interests):

    data = pd.DataFrame({

        "technical_interest": [
            student_interests["technical_interest"]
        ],

        "sports_interest": [
            student_interests["sports_interest"]
        ],

        "cultural_interest": [
            student_interests["cultural_interest"]
        ]

    })

    prediction = model.predict(data)

    return prediction[0]


if __name__ == "__main__":

    student = {
        "technical_interest": 9,
        "sports_interest": 2,
        "cultural_interest": 1
    }

    print("Recommended Event:")
    print(recommend_events(student))