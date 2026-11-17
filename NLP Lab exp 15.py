import nltk
from nltk import PCFG
from nltk.parse import ViterbiParser

print("==========================================")
print("       PCFG PARSING USING PYTHON")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

grammar = PCFG.fromstring("""
S -> NP VP [1.0]
NP -> Det N [0.7] | 'alice' [0.3]
VP -> V NP [0.8] | V [0.2]
Det -> 'an' [0.5] | 'the' [0.5]
N -> 'engineer' [0.4] | 'robot' [0.3] | 'machine' [0.3]
V -> 'designs' [0.5] | 'builds' [0.5]
""")

parser = ViterbiParser(grammar)

sentence = input("\nEnter a sentence: ").lower().split()

print("\nProbabilistic Parsing Results:")
print("--------------------------------")

found = False

for tree in parser.parse(sentence):
    print(tree)
    print("Probability:", tree.prob())
    found = True

if not found:
    print("No valid parse found.")

print("\nPCFG Parsing Completed Successfully.")
print("Program Executed by: C. G. Charishma")
