import tensorflow as tf
import cv2
import numpy as np

# Load model
model = tf.saved_model.load("models/final_model")
infer = model.signatures["serving_default"]

labels = ['angry','disgust','fear','happy','neutral','sad','surprise']

# Face detector
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
)

def predict_emotion(image_path):
    img = cv2.imread(image_path)

    if img is None:
        raise ValueError("Image not found")

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    # Detect faces
    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.1,
        minNeighbors=3,
        minSize=(30, 30)
    )

    # ✅ FIXED LOGIC (NO DUPLICATION)
    if len(faces) == 0:
        # fallback
        face = img
    else:
        x, y, w, h = faces[0]
        face = img[y:y+h, x:x+w]

    # Resize
    face = cv2.resize(face, (224, 224))

    # Normalize
    face = face / 255.0

    face = np.expand_dims(face, axis=0)
    face = tf.convert_to_tensor(face, dtype=tf.float32)

    # Predict
    preds = infer(face)
    preds = list(preds.values())[0].numpy()

    emotion_index = np.argmax(preds)
    confidence = np.max(preds)

    emotion = labels[emotion_index]

    # Better threshold
    if confidence < 0.3:
        emotion = f"Uncertain (maybe {labels[emotion_index]})"
    return emotion, confidence