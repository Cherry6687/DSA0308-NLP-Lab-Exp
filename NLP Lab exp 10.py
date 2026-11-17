import nltk
from nltk.tokenize import word_tokenize

nltk.download('punkt')
nltk.download('punkt_tab')

print("==========================================")
print("    TRANSFORMATION-BASED POS TAGGING")
print("    Student Name: C. G. Charishma")
print("    Register Number: 192472193")
print("==========================================")

text = input("\nEnter a sentence: ")

words = word_tokenize(text)

tagged_words = []

# Initial tagging
for word in words:
    if word.isalpha():
        tag = "NN"
    else:
        tag = "."

    tagged_words.append([word, tag])

# Transformation rules
for item in tagged_words:
    word = item[0].lower()

    if word.endswith("ing"):
        item[1] = "VBG"
    elif word.endswith("ed"):
        item[1] = "VBD"
    elif word.endswith("ly"):
        item[1] = "RB"
    elif word.endswith("s") and word.isalpha():
        item[1] = "NNS"

print("\nTransformation-Based Tagging Results:")
print("--------------------------------")

for word, tag in tagged_words:
    print(word, "----->", tag)

print("\nTagging Completed Successfully.")
print("Program Executed by: C. G. Charishma")
