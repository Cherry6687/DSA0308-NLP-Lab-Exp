
import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

print("==========================================")
print("       PARSE TREE GENERATION USING CFG")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'boy' | 'girl' | 'dog' | 'cat'
V -> 'sees' | 'likes' | 'loves'
""")

parser = RecursiveDescentParser(grammar)

sentence = input("\nEnter a sentence: ").lower().split()

print("\nParse Tree:")
print("--------------------------------")

found = False

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    found = True

if not found:
    print("No valid parse tree found.")

print("\nParse Tree Generated Successfully.")
print("Program Executed by: C. G. Charishma")
