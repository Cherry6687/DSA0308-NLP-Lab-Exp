
import nltk
from nltk import CFG
from nltk.parse import EarleyChartParser

print("==========================================")
print("          EARLEY PARSER USING NLTK")
print("          Student Name: C. G. Charishma")
print("          Register Number: 192472193")
print("==========================================")

grammar = CFG.fromstring("""
S -> NP VP
NP -> Det N
VP -> V NP
Det -> 'the' | 'a'
N -> 'cat' | 'dog' | 'boy'
V -> 'sees' | 'likes'
""")

parser = EarleyChartParser(grammar)

sentence = input("\nEnter a sentence: ").lower().split()

print("\nEarley Parsing Results:")
print("--------------------------------")

found = False

for tree in parser.parse(sentence):
    print(tree)
    tree.pretty_print()
    found = True

if not found:
    print("No valid parse found.")

print("\nEarley Parsing Completed Successfully.")
print("Program Executed by: C. G. Charishma")
