import re

# Function to recognize dialog acts
def recognize_dialog_act(sentence):

    sentence = sentence.lower().strip()

    if re.search(r'\b(hello|hi|hey|good morning|good evening)\b', sentence):
        return "Greeting"

    elif sentence.endswith("?"):
        return "Question"

    elif re.search(r'\b(please|could you|can you|would you)\b', sentence):
        return "Request"

    elif re.search(r'\b(yes|no|okay|sure|thanks|thank you)\b', sentence):
        return "Response"

    else:
        return "Statement"


# Input conversation
dialog = [
    "Hello!",
    "How are you?",
    "I am fine.",
    "Can you help me?",
    "Yes, sure.",
    "Thank you!"
]

# Recognize dialog acts
print("Dialog Act Recognition:\n")

for sentence in dialog:
    act = recognize_dialog_act(sentence)
    print("Sentence:", sentence)
    print("Dialog Act:", act)
    print()
#DONE BY:CHARISHMA(192472193)
