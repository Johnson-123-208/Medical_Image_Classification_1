# 🩺 Pneumonia Detection from Chest X-ray  
### Powered by Deep Learning and Streamlit  
> Developed with ❤️ by **Johnson Obhalloju**

---

## 🚀 About the Project

This is a **real-time Pneumonia Detection web app** built using **TensorFlow**, **Streamlit**, and deep learning. The app predicts whether a chest X-ray image shows signs of **Pneumonia** or is **Normal** using a trained CNN model.

✨ Features include:
- 🎨 Fully animated, full-screen UI with **gradient background themes**
- 🌓 Dark/Light/Red/Purple **theme toggle switch**
- 🗣️ Voice output for predictions
- 🌀 Background particles animation
- 📸 X-ray image uploader
- 🎯 Deep learning prediction with confidence
- 🔮 Interactive Lottie animations

---

## 🌟 Features

| Feature                 | Description                                            |
--------------------------------------------------------------------------------------
| 🧠 Deep Learning Model  | CNN trained on chest X-ray images                      |
| 📤 Upload Image         | Upload `.jpg`, `.jpeg`, or `.png` images               |
| 🔍 Predict Pneumonia    | Classify as **Pneumonia** or **Normal**                |
| 🎙️ Voice Output         | Speaks prediction aloud                                |
| 🎨 Theme Switcher       | Toggle between Light, Dark, Red, Purple themes         |
| 🌀 Particles Background | Animated and responsive background effect              |
| 🖼️ Lottie Animations    | Engaging visuals for scanner and result display        |

---

## 📁 Folder Structure

```
Medical_Image_Classification/
├── app.py                  # Streamlit web app file
├── model/
│   └── medical_cnn.h5      # Trained CNN model file
├── requirements.txt        # All Python dependencies
└── README.md               # This file
```

---

## ⚙️ Installation
1. **Clone this repository**
```bash
git clone https://github.com/your-username/medical-image-classification
cd medical-image-classification
```

2. **Install required packages**

```bash
pip install -r requirements.txt
```

3. **Run the web app**

```bash
streamlit run app.py
```

---

## 📷 How to Use

1. Upload a chest X-ray image from your system.
2. Click **"Predict"** to analyze the image.
3. Listen to the voice output.
4. Switch between themes using the 🎨 toggle at the top-right corner.
5. Enjoy a fully animated and immersive interface.

---

## 🧠 Model Details
- Model: **Convolutional Neural Network (CNN)**
- Framework: **TensorFlow / Keras**
- Dataset: [Chest X-ray Pneumonia (Kaggle)](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- Classes: Binary (Pneumonia / Normal)
- Image Input Size: **150x150 (RGB)**

---

## 📦 `requirements.txt`
```
streamlit
tensorflow
numpy
pillow
streamlit-lottie
requests
gTTS
pygame
```

---

## 💡 Future Enhancements

- 📹 Real-time webcam X-ray classification
- 🌐 Integration with hospital systems
- 🤖 Explainable AI (XAI) for heatmap visualizations

---

## 🙌 Credits

- Dataset: [Kaggle - Chest X-ray Images](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia)
- Lottie Animations: [LottieFiles](https://lottiefiles.com)
- Particles.js Integration: [Vincent Garreau](https://vincentgarreau.com/particles.js)

---

## 🛡️ Disclaimer

> This application is for **educational purposes only**. It is not intended for real-world medical diagnosis. Please consult a medical professional for accurate healthcare advice.

---
