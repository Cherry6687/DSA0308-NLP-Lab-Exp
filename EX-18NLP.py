import re

def parse_fopc(expression):
    print("Input Expression:", expression)

    # Identify logical operators
    operators = {
        "&": "AND",
        "|": "OR",
        "~": "NOT",
        "->": "IMPLIES",
        "<->": "IFF"
    }

    print("\nParsed Expression:")

    for op, meaning in operators.items():
        expression = expression.replace(op, " " + meaning + " ")

    # Find predicates and their arguments
    predicates = re.findall(r'[A-Za-z]+\([^()]*\)', expression)

    for p in predicates:
        print("Predicate:", p)

    # Find variables and constants
    arguments = re.findall(r'\((.*?)\)', expression)

    for arg in arguments:
        print("Arguments:", arg)

    print("\nLogical Expression Parsed Successfully!")


# Main program
expr = "Human(Socrates) & Mortal(Socrates)"
parse_fopc(expr)
