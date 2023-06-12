if __name__ == '__main__':
    from training_data import data

    from sklearn.feature_extraction.text import CountVectorizer
    from sklearn.naive_bayes import MultinomialNB
    import pickle

    phrase = [item['phrase'].translate({ord(i): None for i in '፣።፤'}) for item in data]
    # Create feature vectors using CountVectorizer
    vectorizer = CountVectorizer()
    X = vectorizer.fit_transform(phrase)

    # Create the classifier
    classifier = MultinomialNB()
    classifier.fit(X, [item["solution"].translate({ord(i): None for i in '፣።፤'}) for item in data])

    # Save the trained model
    with open("model.pkl", "wb") as f:
        pickle.dump((vectorizer, classifier), f)
    print("learning our machine is done!")

