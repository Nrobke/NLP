if __name__ == '__main__':
    from train_data import data

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    import pickle

    # Create feature vectors using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform([item['phrase'] for item in data])

    # Create the classifier
    classifier = MultinomialNB()
    classifier.fit(X, [item["solution"] for item in data])

    # Save the trained model
    with open("model.pkl", "wb") as f:
        pickle.dump((vectorizer, classifier), f)
    print("learning our machine is done!")