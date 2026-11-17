from transformers import pipeline

# Load translation model
translator = pipeline("translation_en_to_fr",
                      model="Helsinki-NLP/opus-mt-en-fr")

# Input English text
text = "Hello, how are you?"

# Translate English to French
result = translator(text)

# Display translated text
print("English Text:", text)
print("French Translation:", result[0]['translation_text'])
