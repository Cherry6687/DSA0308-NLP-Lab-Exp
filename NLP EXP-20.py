from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Sample documents
documents = [
    "Artificial Intelligence is transforming the world",
    "Machine Learning is a part of Artificial Intelligence",
    "Python is used for Data Science and Machine Learning",
    "Deep Learning is a branch of Machine Learning"
]

# Input search query
query = "Machine Learning"

# Create TF-IDF vectorizer
vectorizer = TfidfVectorizer()

# Convert documents into TF-IDF vectors
tfidf_matrix = vectorizer.fit_transform(documents)

# Convert query into TF-IDF vector
query_vector = vectorizer.transform([query])

# Calculate cosine similarity
similarity = cosine_similarity(query_vector, tfidf_matrix)

# Rank documents based on similarity
ranked_docs = similarity.flatten().argsort()[::-1]

# Display ranked results
print("Search Query:", query)
print("\nDocument Ranking:")

for i, index in enumerate(ranked_docs):
    print(f"Rank {i+1}: {documents[index]}")
    print("Similarity Score:", round(similarity[0][index], 3))


#done by:CHARISHMA(192472193)
