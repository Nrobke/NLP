import pickle


import sys
import os


def answer(question: str = None):
    # Load the saved model
    model_path = os.path.join(os.path.dirname(os.getcwd()), "Ai/model.pkl")
    with open(model_path, "rb") as f:
        vectorizer, classifier = pickle.load(f)

        # Example usage
        if question is None :
            question = sys.argv[1]
            question = input("insert: ")

        # Preprocess the question using the same vectorizer
        X_test = vectorizer.transform([question])

        # Make predictions using the loaded classifier
        predicted_solution = classifier.predict(X_test)
        probabilities = classifier.predict_proba(X_test)

        confidence = probabilities.max()

        print("Predicted solution:", predicted_solution[0])
        print("Confidence:", round(confidence * 100, 4), " %")

        return {
            "answer": predicted_solution[0].replace('\n', ''),
            'confidence': f"{round(confidence * 100)}፨"
        }
