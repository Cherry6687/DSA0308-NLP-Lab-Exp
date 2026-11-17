from openai import OpenAI

# Create OpenAI client
client = OpenAI(api_key="YOUR_API_KEY")

# Given prompt
prompt = "Explain Artificial Intelligence in simple words."

# Generate text
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": prompt}
    ],
    max_tokens=100
)

# Display generated text
print("Generated Text:")
print(response.choices[0].message.content)
