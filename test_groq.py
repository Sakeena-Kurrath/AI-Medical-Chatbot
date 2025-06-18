from groq import Groq

# DIRECT KEY TEST - Replace with your actual key
TEST_KEY = "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"  # 👈 Replace this!

client = Groq(api_key=TEST_KEY)

try:
    test = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello"}],
        model="llama3-8b-8192"
    )
    print("✅ Key works! Response:", test.choices[0].message.content)
except Exception as e:
    print("❌ Key failed:", e)