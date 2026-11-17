
print("==========================================")
print(" FINITE STATE MACHINE FOR MORPHOLOGICAL PARSING")
print(" Student Name: C. G. Charishma")
print(" Register Number: 192472193")
print("==========================================")

def plural_fsm(noun):

    print("\nOriginal Noun:", noun)

    if noun.endswith(("s", "sh", "ch", "x", "z")):
        plural = noun + "es"
        state = "State 1: Add 'es'"

    elif noun.endswith("y") and len(noun) > 1 and noun[-2].lower() not in "aeiou":
        plural = noun[:-1] + "ies"
        state = "State 2: Replace 'y' with 'ies'"

    else:
        plural = noun + "s"
        state = "State 3: Add 's'"

    print(state)
    print("Plural Form:", plural)


print("\nFINITE STATE MACHINE - PLURAL NOUN GENERATOR")

n = int(input("\nEnter the number of nouns: "))

for i in range(n):
    noun = input("\nEnter a noun: ")
    plural_fsm(noun)

print("\nMorphological Parsing Completed Successfully.")
print("Program Executed by: C. G. Charishma")
