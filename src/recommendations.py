import random

# 🔥 10 REAL-WORLD ACTIVITIES PER EMOTION

ACTIVITIES = {

    "sad": [
        "Go for a 10-minute walk outside 🌿",
        "Listen to your favorite music 🎧",
        "Call a close friend or family member 📞",
        "Write your thoughts in a journal 📓",
        "Watch a light or funny video 🎬",
        "Sit in sunlight for a few minutes ☀️",
        "Practice deep breathing for 5 minutes 🌬",
        "Clean your room or workspace 🧹",
        "Read 5–10 pages of a book 📖",
        "Drink water and take care of your body 💧"
    ],

    "angry": [
        "Take 10 deep breaths slowly 🧘",
        "Do 20 pushups or quick exercise 💪",
        "Go for a fast walk or run 🏃",
        "Drink water and step away 💧",
        "Listen to calming music 🎵",
        "Write down what made you angry ✍️",
        "Take a short break from people ⏸",
        "Splash cold water on your face ❄️",
        "Stretch your body slowly 🧍",
        "Avoid reacting immediately — pause first ⛔"
    ],

    "fear": [
        "Practice slow breathing (4-7-8) 🌬",
        "Sit quietly and observe surroundings 🧠",
        "Talk to someone you trust 🤝",
        "Write your fear and break it into steps ✍️",
        "Watch something calming 🎥",
        "Remind yourself it's temporary 💭",
        "Take small actions instead of avoiding 🪜",
        "Listen to soothing sounds 🎶",
        "Stay in a comfortable environment 🛋",
        "Focus on what you can control 🎯"
    ],

    "neutral": [
        "Learn something new for 15 minutes 📘",
        "Watch an inspiring video 🎥",
        "Do a small productive task ✅",
        "Go for a short walk 🚶",
        "Organize your schedule 📅",
        "Try a new hobby 🎨",
        "Read an article or blog 📰",
        "Talk to a friend casually 💬",
        "Listen to a podcast 🎧",
        "Set a small goal for today 🎯"
    ],

    "happy": [
        "Share your happiness with someone 😊",
        "Keep doing what you enjoy 🎉",
        "Help someone else 🤝",
        "Write what made you happy ✨",
        "Celebrate small wins 🎊",
        "Capture the moment (photo/video) 📸",
        "Spend time with loved ones ❤️",
        "Try something creative 🎨",
        "Express gratitude 🙏",
        "Stay consistent with good habits 💪"
    ],

    "surprise": [
        "Take a moment to process what happened 🤔",
        "Share your experience with someone 😄",
        "Write down your thoughts ✍️",
        "Reflect on why it surprised you 🧠",
        "Stay calm and observe 🔍",
        "Turn it into a learning moment 📘",
        "Take a deep breath and relax 🌬",
        "Avoid quick decisions ⛔",
        "Look at the positive side 😊",
        "Give yourself time to adjust ⏳"
    ],

    "disgust": [
        "Step away from the situation 🚶",
        "Take fresh air 🌿",
        "Wash your face or hands 💧",
        "Change your environment 🏠",
        "Distract yourself with something positive 🎧",
        "Avoid thinking too much about it 🧠",
        "Focus on something clean/pleasant 🌸",
        "Drink water and reset 💧",
        "Talk to someone if needed 🤝",
        "Move on and refocus 🎯"
    ]
}


# 🔥 FUNCTION TO GET ALL 10 TIPS
def get_all_recommendations(emotion):
    return ACTIVITIES.get(emotion, ["Take care of yourself ❤️"])


# 🔥 FUNCTION TO GET ONE RANDOM (FOR CHATBOT)
def get_random_recommendation(emotion, history):

    past = [chat.get("recommendation") for chat in history if "recommendation" in chat]

    possible = ACTIVITIES.get(emotion, [])

    new_options = [act for act in possible if act not in past]

    if not new_options:
        new_options = possible

    return random.choice(new_options)