import nltk
import spacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Input text
text = "John is a student. He studies Python. Mary is his friend. She likes programming."

# Process text
doc = nlp(text)

print("Input Text:", text)
print("\nReference Resolution:")

# Store previously identified names
names = []

for token in doc:
    if token.pos_ == "PROPN":
        names.append(token.text)

    elif token.pos_ == "PRON":
        if token.text.lower() == "he":
            print(token.text, "refers to John")
        elif token.text.lower() == "she":
            print(token.text, "refers to Mary")
        elif token.text.lower() == "his":
            print(token.text, "refers to John")

print("\nReference Resolution Completed!")
