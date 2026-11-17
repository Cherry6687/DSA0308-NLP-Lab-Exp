
import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

print("==========================================")
print("       PART-OF-SPEECH TAGGING USING NLTK")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

text = input("\nEnter a sentence: ")

words = word_tokenize(text)

tags = pos_tag(words)

print("\nPOS Tagging Results:")
print("--------------------------------")

for word, tag in tags:
    print(word, "----->", tag)

print("\nPOS Tagging Completed Successfully.")
print("Program Executed by: C. G. Charishma")
