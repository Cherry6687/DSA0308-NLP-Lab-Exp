import nltk
from nltk.wsd import lesk
from nltk.corpus import wordnet

# Download required datasets
nltk.download('wordnet')
nltk.download('omw-1.4')

# Input sentence
sentence = "I went to the bank to deposit money"

# Convert sentence into words
words = sentence.split()

# Ambiguous word
target_word = "bank"

# Apply Lesk algorithm
sense = lesk(words, target_word)

# Display result
print("Sentence:", sentence)
print("Target Word:", target_word)

if sense:
    print("Word Sense:", sense.name())
    print("Meaning:", sense.definition())
else:
    print("No meaning found")


#DONE BY:CHARISHMA(192472193)
