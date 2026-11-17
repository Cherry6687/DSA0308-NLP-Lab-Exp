import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag
from nltk.probability import FreqDist, ConditionalFreqDist

nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger_eng')

print("==========================================")
print("    STOCHASTIC POS TAGGING")
print("    Student Name: C. G. Charishma")
print("    Register Number: 192472193")
print("==========================================")

text = input("\nEnter a sentence: ")

words = word_tokenize(text.lower())

training_text = "Charishma studies artificial intelligence. She writes Python programs. Students learn new technologies. Artificial intelligence helps people."

train_words = word_tokenize(training_text.lower())
tagged_words = pos_tag(train_words)

# Build a probabilistic model
word_tag_model = ConditionalFreqDist()

for word, tag in tagged_words:
    word_tag_model[word][tag] += 1

print("\nStochastic POS Tagging Results:")
print("--------------------------------")

for word in words:
    if word in word_tag_model:
        tag = word_tag_model[word].max()
    else:
        tag = "NN"
    print(word, "----->", tag)

print("\nPOS Tagging Completed Successfully.")
print("Program Executed by: C. G. Charishma")
