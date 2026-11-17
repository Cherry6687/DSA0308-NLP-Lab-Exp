import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

# Given input text
text = """Apple was founded by Steve Jobs in California in 1976.
Microsoft is located in the United States."""

# Process the text
doc = nlp(text)

# Display named entities
print("Named Entities:")
for ent in doc.ents:
    print(ent.text, " - ", ent.label_)

#done by;charishma(192472193)
