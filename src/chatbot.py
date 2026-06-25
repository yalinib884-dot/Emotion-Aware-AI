import os
from dotenv import load_dotenv
from groq import Groq
# 🔥 Load environment variables
load_dotenv()
# 🔥 Load multiple API keys
API_KEYS = [
    os.getenv("GROQ_API_KEY_1"),
    os.getenv("GROQ_API_KEY_2"),
    os.getenv("GROQ_API_KEY_3")
]

# Remove None keys
API_KEYS = [key for key in API_KEYS if key]

if not API_KEYS:
    raise ValueError("No GROQ API keys found. Check your .env file")

# 🔁 Round Robin index
key_index = 0


# 🔁 Get next API client
def get_next_client():
    global key_index
    api_key = API_KEYS[key_index]
    key_index = (key_index + 1) % len(API_KEYS)
    return Groq(api_key=api_key)


# 🎯 MAIN FUNCTION
def generate_ai_response(emotion, user_message):

    for _ in range(len(API_KEYS)):  # try all keys
        try:
            client = get_next_client()

            # 🔥 Prompt (emotion-aware)
            prompt = f"""
            The user is feeling: {emotion}

            User message: {user_message}

            Instructions:
            - Be supportive and empathetic
            - Keep response short
            - Do NOT give medical advice

            Format:
            Support Response:
            <text>

            Suggested Activity:
            <text>

            Reflection Question:
            <text>
            """

            # 🔥 API CALL (FINAL WORKING MODEL)
            response = client.chat.completions.create(
                model="llama-3.1-8b-instant",
                messages=[
                    {"role": "system", "content": "You are a helpful emotional support assistant."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.7
            )

            return response.choices[0].message.content

        except Exception as e:
            print("❌ Key failed:", e)
            continue

    return "⚠️ All API keys exhausted. Please try again later."