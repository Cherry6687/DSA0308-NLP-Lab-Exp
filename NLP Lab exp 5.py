
import nltk
from nltk.stem import PorterStemmer

nltk.download('punkt')

stemmer = PorterStemmer()

print("==========================================")
print("       PORTER STEMMER ALGORITHM")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

text = input("\nEnter a sentence: ")

words = nltk.word_tokenize(text)

print("\nOriginal Words and Stemmed Words")
print("------------------------------------------")

for word in words:
    if word.isalpha():
        stemmed_word = stemmer.stem(word)
        print(word, "------>", stemmed_word)

print("\nWord Stemming Completed Successfully.")
print("Program Executed by: C. G. Charishma")
