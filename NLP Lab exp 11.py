
import nltk
from nltk import CFG
from nltk.parse import RecursiveDescentParser

print("==========================================")
print("       TOP-DOWN PARSER USING CFG")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'boy'
V -> 'sees' | 'likes'
""")

parser = RecursiveDescentParser(grammar)

sentence = input("\nEnter a sentence: ").lower().split()

print("\nParsing Results:")
print("--------------------------------")

found = False

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    found = True

if not found:
    print("No valid parse found.")

print("\nParsing Completed Successfully.")
print("Program Executed by: C. G. Charishma")
