import nltk
from nltk import word_tokenize, pos_tag, RegexpParser
from nltk.corpus import wordnet

# Download required datasets
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

# Input sentence
sentence = "The intelligent student reads a book in the library."

# Tokenization
words = word_tokenize(sentence)

# POS Tagging
tagged_words = pos_tag(words)

# Define grammar for noun phrases
grammar = "NP: {<DT>?<JJ>*<NN.*>+}"

# Create parser
parser = RegexpParser(grammar)

# Parse sentence
tree = parser.parse(tagged_words)

print("Input Sentence:", sentence)
print("\nNoun Phrases and Their Meanings:")

# Extract noun phrases
for subtree in tree.subtrees(filter=lambda t: t.label() == 'NP'):
    phrase = " ".join(word for word, tag in subtree.leaves())
    print("\nNoun Phrase:", phrase)

    # Find meaning using WordNet
    noun = next(
        (word for word, tag in subtree.leaves() if tag.startswith('NN')),
        None
    )

    if noun:
        synsets = wordnet.synsets(noun, pos=wordnet.NOUN)

        if synsets:
            print("Meaning:", synsets[0].definition())
        else:
            print("Meaning: Not found in WordNet")

#DONE BY:CHARISHMA(192472193)
