import pickle

import sys
import os


def answer(question: str = None):
    # Load the saved model
    model_path = os.path.join(os.path.dirname(os.getcwd()), "Ai/model.pkl")
    with open(model_path, "rb") as f:
        vectorizer, classifier = pickle.load(f)

        # Example usage
        if question is None:
            question = input("insert: ")

        # Preprocess the question using the same vectorizer
        X_test = vectorizer.transform([question])

        # Make predictions using the loaded classifier
        predicted_solution = classifier.predict(X_test)
        probabilities = classifier.predict_proba(X_test)

        confidence = probabilities.max()

        print("Predicted solution:", predicted_solution[0])
        print("Confidence:", round(confidence * 100, 4), " %")

        gold_wax = predicted_solution[0].split('\n')

        return {
            "answer": predicted_solution[0].replace('\n', ''),
            "word": gold_wax[0],
            "wax": gold_wax[1],
            "gold": gold_wax[2],
            'confidence': f"{round(confidence * 100, 2)}%"
        }


if __name__ == "__main__":
    answer()
