
import re

# Given text
text = "I want to travel from chennai to madurai in train in platform no 3"

# Search for Chennai
if re.search(r"chennai", text, re.IGNORECASE):
    text = re.sub(r"chennai", "bangalore", text, flags=re.IGNORECASE)

# Search for Madurai
if re.search(r"madurai", text, re.IGNORECASE):
    text = re.sub(r"madurai", "coimbatore", text, flags=re.IGNORECASE)

# Search for train
if re.search(r"train", text, re.IGNORECASE):
    text = re.sub(r"train", "bus", text, flags=re.IGNORECASE)

# Search for platform number
if re.search(r"\bplatform no \d+\b", text, re.IGNORECASE):
    text = re.sub(r"\bplatform no \d+\b", "platform no 5", text, flags=re.IGNORECASE)

# Display the modified text
print("Updated Text:", text)
