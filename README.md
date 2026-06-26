# 🧠 Emotion-Aware AI Assistant

An intelligent AI-powered system that detects human emotions from images, engages users through a conversational chatbot, and provides personalized activity-based recommendations along with emotional insights.

---

## 🎥 Project Demo

▶️ **Watch the Demo:**  
https://youtu.be/0XU9FvmU45w?si=c-0mqOgsVWwQOeE1



## 🚀 Features

### 🖼 Emotion Detection

* Detects user emotions from uploaded images
* Uses deep learning (TensorFlow-based model)
* Supports multiple emotions:
  `Happy, Sad, Angry, Fear, Neutral, Surprise, Disgust`

---

### 🤖 AI Chatbot (ChatGPT-style UI)

* Interactive conversational interface
* Emotion-aware responses using LLM (Groq API)
* Maintains chat history for better interaction

---

### 💡 Activity-Based Recommendation System

* Provides **real-world actionable suggestions**
* 10 personalized tips per emotion
* Avoids repetition using session memory
* Helps users improve emotional well-being

---

### 📊 Analytics Dashboard

* Emotion distribution visualization
* Mood trend analysis
* Positive vs Negative emotional insights
* Helps users understand emotional patterns

---

## 🛠 Tech Stack

* **Frontend:** Streamlit
* **Backend:** Python
* **AI/ML:** TensorFlow, OpenCV
* **LLM API:** Groq
* **Data Visualization:** Streamlit Charts

---

## 📂 Project Structure

```
Emotion-AI/
│
├── dashboard/
│   └── app.py              # Main Streamlit UI
│
├── src/
│   ├── predict.py          # Emotion detection logic
│   ├── chatbot.py          # AI chatbot integration
│   ├── recommender.py      # Activity recommendation system
│
├── models/                 # Trained ML model (not included)
├── .env                    # API keys (ignored)
├── requirements.txt        # Dependencies
└── README.md
```

---

## ⚙️ Installation & Setup

### 1️⃣ Create Virtual Environment

```bash
python -m venv emotion_env
emotion_env\Scripts\activate   # Windows
```

### 2️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Add API Keys

Create a `.env` file in the root folder:

```env
GROQ_API_KEY_1=your_key_here
GROQ_API_KEY_2=your_key_here
GROQ_API_KEY_3=your_key_here
```

### 4️⃣ Run the Application

```bash
streamlit run dashboard/app.py
```

---

## 🧠 System Workflow

1. User uploads an image
2. Emotion is detected using a deep learning model
3. Chatbot interacts based on detected emotion
4. Recommendation system suggests real-life activities
5. Dashboard visualizes emotional patterns

---

## 🎯 Key Highlights

* Emotion-aware AI system (Computer Vision + NLP)
* ChatGPT-style conversational UI
* Activity-based recommendation system (10 tips per emotion)
* Emotion analytics dashboard with insights
* Session-based memory for better user experience

---

## ⚠️ Important Notes

* Model files are not included due to size limitations
* API keys are excluded for security reasons
* Use your own API keys in `.env`

---

## 🚀 Future Enhancements

* Real-time webcam emotion detection
* User authentication system
* Persistent database (MongoDB / SQLite)
* Cloud deployment (AWS / GCP / Streamlit Cloud)

---

## ⭐ Support

If you found this project useful, consider giving it a star ⭐
