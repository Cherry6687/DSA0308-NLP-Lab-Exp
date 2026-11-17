from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Input text
text = """Artificial Intelligence is growing rapidly.
Machine Learning is a part of Artificial Intelligence.
Machine Learning helps computers learn from data.
Python is widely used for Machine Learning."""

# Split text into sentences
sentences = text.split(".")

# Remove empty sentences
sentences = [s.strip() for s in sentences if s.strip()]

# Calculate TF-IDF
vectorizer = TfidfVectorizer()
tfidf_matrix = vectorizer.fit_transform(sentences)

# Calculate similarity between consecutive sentences
scores = []

print("Sentence Coherence Scores:")

for i in range(len(sentences) - 1):
    score = cosine_similarity(
        tfidf_matrix[i], tfidf_matrix[i + 1]
    )[0][0]

    scores.append(score)

    print("Sentence", i + 1, "and Sentence", i + 2,
          ":", round(score, 3))

# Calculate overall coherence
if scores:
    coherence = sum(scores) / len(scores)

    print("\nOverall Coherence Score:", round(coherence, 3))

    if coherence >= 0.3:
        print("Text Coherence: Good")
    else:
        print("Text Coherence: Low")
#DONE BY:CHARISHMA(192472193)
