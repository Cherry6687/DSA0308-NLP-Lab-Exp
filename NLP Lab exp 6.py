
import random
import nltk
from nltk.util import bigrams
from nltk.tokenize import word_tokenize
from collections import defaultdict

nltk.download('punkt')
nltk.download('punkt_tab')

print("==========================================")
print("       BIGRAM MODEL FOR TEXT GENERATION")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

text = input("\nEnter a sentence: ")

words = word_tokenize(text.lower())

bigram_model = defaultdict(list)

for w1, w2 in bigrams(words):
    bigram_model[w1].append(w2)

start_word = input("\nEnter the starting word: ").lower()

generated_text = [start_word]

for i in range(9):
    current_word = generated_text[-1]

    if current_word in bigram_model:
        next_word = random.choice(bigram_model[current_word])
        generated_text.append(next_word)
    else:
        break

print("\nGenerated Text:")
print(" ".join(generated_text))

print("\nText Generation Completed Successfully.")
print("Program Executed by: C. G. Charishma")
