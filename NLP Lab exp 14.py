
import nltk
from nltk import CFG
from nltk.parse import ChartParser

print("==========================================")
print("       SUBJECT-VERB AGREEMENT CHECKER")
print("       Student Name: C. G. Charishma")
print("       Register Number: 192472193")
print("==========================================")

grammar = CFG.fromstring("""
S -> NP_S VP_S | NP_P VP_P
NP_S -> Det_S N_S
NP_P -> Det_P N_P
VP_S -> V_S
VP_P -> V_P
Det_S -> 'the'
Det_P -> 'the'
N_S -> 'boy' | 'girl' | 'student'
N_P -> 'boys' | 'girls' | 'students'
V_S -> 'runs' | 'plays' | 'writes'
V_P -> 'run' | 'play' | 'write'
""")

parser = ChartParser(grammar)

sentence = input("\nEnter a sentence: ").lower().split()

print("\nAgreement Checking Result:")
print("--------------------------------")

found = False

for tree in parser.parse(sentence):
    print(tree)
    print("Subject-Verb Agreement: Correct")
    found = True

if not found:
    print("Subject-Verb Agreement: Incorrect")

print("\nAgreement Checking Completed Successfully.")
print("Program Executed by: C. G. Charishma")
