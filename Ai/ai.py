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

        if not question:
            return {"success": "false", "response": "Please insert a poem (ቅኔ)"}


        # Preprocess the question using the same vectorizer
        X_test = vectorizer.transform([question])

        # Make predictions using the loaded classifier
        predicted_solution = classifier.predict(X_test)
        probabilities = classifier.predict_proba(X_test)

        confidence = round(probabilities.max() * 100, 2)

        if confidence < 1.5:
            return {"success": False, "response": f"As an AI model my responses are based on the information I have been trained on and may not encompass all poems (ቅኔዎች)\t confidence: {confidence}%"}
        elif confidence > 2 and confidence < 25:
            return {"success": False, "response": f"Could you insert the whole poem (ቅኔ)?, I can not provide the answer based on the given information\t confidence: {confidence}%"}


        print("Predicted solution:", predicted_solution[0])
        print("Confidence:", confidence, " %")

        gold_wax = predicted_solution[0].split('\n')



        return {
            "success": True,
            "answer": predicted_solution[0].replace('\n', ''),
            "word": gold_wax[0],
            "wax": gold_wax[1],
            "gold": gold_wax[2],
            'confidence': f"{confidence}%"
        }


if __name__ == "__main__":
    answer()
