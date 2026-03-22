from sklearn.feature_extraction.text import TfidfVectorizer


def extract_keywords(text, top_n=10):
    if not text.strip():
        return []

    vectorizer = TfidfVectorizer(
        stop_words="english",
        ngram_range=(1, 2),      # includes single words + phrases
        max_features=100,
        lowercase=True
    )

    tfidf_matrix = vectorizer.fit_transform([text])

    feature_names = vectorizer.get_feature_names_out()
    scores = tfidf_matrix.toarray()[0]

    word_scores = list(zip(feature_names, scores))

    # sort by importance
    sorted_words = sorted(word_scores, key=lambda x: x[1], reverse=True)

    # filter out very short words 
    keywords = [
        word for word, score in sorted_words
        if len(word) > 2
    ]

    return keywords[:top_n]