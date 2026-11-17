
import nltk
from nltk.stem import PorterStemmer
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

stemmer = PorterStemmer()

def morphological_analysis(word):
    print("\nOriginal Word:", word)

    root = stemmer.stem(word)
    print("Root Word:", root)

    prefixes = ["un", "re", "dis", "pre", "mis", "in", "im"]
    suffixes = ["ing", "ed", "er", "est", "ly", "ness", "ment", "ful"]

    prefix = "None"
    suffix = "None"

    for p in prefixes:
        if word.lower().startswith(p) and len(word) > len(p):
            prefix = p
            break

    for s in suffixes:
        if word.lower().endswith(s) and len(word) > len(s):
            suffix = s
            break

    print("Prefix:", prefix)
    print("Suffix:", suffix)

    if prefix != "None" or suffix != "None":
        print("Morphological Analysis: Affixes identified")
    else:
        print("Morphological Analysis: No matching affixes found")


print("==========================================")
print("   MORPHOLOGICAL ANALYSIS USING NLTK")
print("   Student Name: C. G. Charishma")
print("   Register Number: 192472193")
print("==========================================")

text = input("\nEnter your sentence: ")

# Predefined input sentence
text = "My name is C. G. Charishma. I am studying Artificial Intelligence and Machine Learning. I am learning Natural Language Processing using Python."

print("Input Sentence:", text)

words = word_tokenize(text)

for word in words:
    if word.isalpha():
        morphological_analysis(word)

print("\nAnalysis Completed Successfully.")
print("Program Executed by: C. G. Charishma")
