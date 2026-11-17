import nltk
from nltk.corpus import wordnet

# Download WordNet dataset
nltk.download('wordnet')
nltk.download('omw-1.4')

# Given word
word = "happy"

# Retrieve synsets
synsets = wordnet.synsets(word)

print("Word:", word)
print("\nSynsets and Meanings:")

for syn in synsets:
    print("\nSynset:", syn.name())
    print("Definition:", syn.definition())
    print("Examples:", syn.examples())
