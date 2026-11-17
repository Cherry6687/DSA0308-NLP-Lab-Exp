
import nltk
from nltk.tokenize import word_tokenize
from nltk import RegexpTagger

nltk.download('punkt')
nltk.download('punkt_tab')

print("==========================================")
print("    RULE-BASED POS TAGGING USING REGEX")
print("    Student Name: C. G. Charishma")
print("    Register Number: 192472193")
print("==========================================")

patterns = [
    (r'.*ing$', 'VBG'),
    (r'.*ed$', 'VBD'),
    (r'.*ly$', 'RB'),
    (r'.*ous$', 'JJ'),
    (r'.*ful$', 'JJ'),
    (r'.*ness$', 'NN'),
    (r'.*ment$', 'NN'),
    (r'.*s$', 'NNS'),
    (r'.*', 'NN')
]

tagger = RegexpTagger(patterns)

text = input("\nEnter a sentence: ")

words = word_tokenize(text)

tags = tagger.tag(words)

print("\nRule-Based POS Tagging Results:")
print("--------------------------------")

for word, tag in tags:
    print(word, "----->", tag)

print("\nPOS Tagging Completed Successfully.")
print("Program Executed by: C. G. Charishma")
