import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
import requests
from streamlit_lottie import st_lottie
import pyttsx3

# Page config
st.set_page_config(page_title="Pneumonia Detector", page_icon="🩺", layout="centered")

# Load Lottie animations
def load_lottie_url(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

lottie_xray = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_wnqlfojb.json")
lottie_result = load_lottie_url("https://assets2.lottiefiles.com/packages/lf20_tutvdkg0.json")

# Theme settings
theme = st.selectbox(
    "", ["Light", "Dark", "Red", "Purple"],
    index=0,
    key="theme_select",
    label_visibility="collapsed"
)

# Custom Theme CSS
theme_css = {
    "Light": {"bg": "#f3f4f6", "text": "#111", "button": "#4CAF50", "border": "#ccc"},
    "Dark": {"bg": "#1e1e2f", "text": "#fff", "button": "#6EE7B7", "border": "#555"},
    "Red": {"bg": "#ffe5e5", "text": "#8B0000", "button": "#FF0000", "border": "#f7a8a8"},
    "Purple": {"bg": "#f3e8ff", "text": "#5B21B6", "button": "#8B5CF6", "border": "#d6b3ff"},
}

colors = theme_css[theme]

# Apply theme styles
st.markdown(f"""
    <style>
    body, .stApp {{
        background-color: {colors['bg']} !important;
        color: {colors['text']} !important;
        transition: all 0.5s ease-in-out;
    }}
    .title {{
        font-size: 30px !important;
        font-weight: bold;
        color: {colors['text']} !important;
        text-align: center;
        margin-bottom: 30px;
    }}
    .stButton > button {{
        background-color: {colors['button']};
        color: white;
        padding: 10px 24px;
        font-size: 18px;
        border: none;
        border-radius: 6px;
        margin-top: 15px;
        transition: 0.3s ease-in-out;
    }}
    .stButton > button:hover {{
        opacity: 0.9;
        transform: scale(1.05);
    }}
    .css-1v0mbdj.e1fqkh3o5 {{  /* Theme dropdown position fix */
        position: absolute;
        top: 20px;
        right: 30px;
        width: 150px !important;
        z-index: 9999;
    }}
    .stFileUploader, .stImage {{
        border: 2px dashed {colors['border']} !important;
        border-radius: 10px;
        padding: 12px;
        margin-bottom: 20px;
        background-color: #ffffff20;
    }}
    </style>
""", unsafe_allow_html=True)

# Load model
model = tf.keras.models.load_model("model/medical_cnn.h5")

# Header
st.markdown('<div class="title">🩺 Pneumonia Detection from Chest X-ray</div>', unsafe_allow_html=True)
st_lottie(lottie_xray, height=250, key="xray")

# File upload
uploaded_file = st.file_uploader("📤 Upload a Chest X-ray Image", type=["jpg", "jpeg", "png"])

if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded Image", use_container_width=True)

    # Preprocess
    img = img.resize((150, 150)).convert("RGB")
    img_array = np.expand_dims(np.array(img) / 255.0, axis=0)

    if st.button("🔍 Predict"):
        prediction = model.predict(img_array)[0][0]
        label = "🛑 PNEUMONIA" if prediction > 0.5 else "✅ NORMAL"
        confidence = prediction if prediction > 0.5 else 1 - prediction

        st_lottie(lottie_result, height=200, key="result")
        #st.success(f"**Prediction: {label}**\n\nConfidence: `{confidence:.2f}`")

        st.markdown(f"""
            <div style="
                background-color: #ffffff20;
                padding: 25px;
                border-radius: 12px;
                border: 2px solid {colors['border']};
                box-shadow: 0px 0px 12px rgba(0,0,0,0.1);
                text-align: center;
                margin-top: 20px;
            ">
                <h2 style='color: {colors['text']}; font-size: 28px;'>🧠 Prediction Result</h2>
                <h1 style='color: {colors['text']}; font-size: 36px;'>{label}</h1>
                <p style='font-size: 20px; color: {colors['text']};'>Confidence: <b>{confidence:.2f}</b></p>
            </div>
        """, unsafe_allow_html=True)
        
        engine = pyttsx3.init()
        engine.say(f"The prediction is {label}. Confidence is {confidence:.2f}")
        engine.runAndWait()

# Footer
st.markdown("---")
st.markdown(
    f"<div style='text-align:center; font-weight:600;'>💡 Developed with ❤️ by <b>Johnson Obhalloju</b></div>",
    unsafe_allow_html=True
)
