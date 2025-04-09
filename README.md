🩺 Pneumonia Detection from Chest X-ray
Powered by Deep Learning and Streamlit
Developed with ❤️ by Johnson Obhalloju

🚀 About the Project
This is a real-time Pneumonia Detection web app built using TensorFlow, Streamlit, and deep learning techniques. The app predicts whether a chest X-ray shows signs of Pneumonia or Normal lungs using a trained Convolutional Neural Network (CNN) model.

It includes:

🎨 Animated, full-screen UI with vibrant theme switching (Light, Dark, Red, Purple)

💬 Voice output for predictions

✨ Background particles animation

🔮 Lottie animations for interactive visuals

📸 X-ray image uploader with live prediction

✅ Fully responsive and stylish interface

🌟 Features
Feature	Description
🧠 Deep Learning Model	CNN trained on chest X-ray images
🖼️ Upload X-ray Image	Upload .jpg, .png, or .jpeg image
🎯 Predict Pneumonia	Get prediction with confidence score
🎙️ Voice Output	App reads out the prediction using text-to-speech
🌈 Theme Toggle	Light, Dark, Red, and Purple themes
🌀 Background Animation	Beautiful interactive particles background
🔁 Real-time Feedback	Lottie animations for scanning and result visuals
📁 Folder Structure
bash
Copy
Edit
Medical_Image_Classification/
├── app.py                  # Main Streamlit app
├── model/
│   └── medical_cnn.h5      # Trained CNN model
├── data/
│   └── (optional dataset for local training/testing)
├── utils/
│   └── helpers.py 
├── requirements.txt
└── README.md
⚙️ Installation
Clone the repo

bash
Copy
Edit
git clone https://github.com/your-username/medical-image-classification
cd medical-image-classification
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Run the app

bash
Copy
Edit
streamlit run app.py
📷 How to Use
Upload a chest X-ray image.

Click "Predict".

Listen to the voice output and view prediction result (Pneumonia / Normal).

Try switching between themes from the top-right 🎨 selector.

🧠 Model Info
Trained using Keras + TensorFlow.

Dataset used: Chest X-ray Images (Pneumonia).

Input shape: (150, 150, 3) — RGB resized images.

Binary classification: Pneumonia vs Normal.

💡 Future Enhancements
Webcam-based real-time detection

Integration with hospital data systems

Extended support for other lung diseases

🙌 Credits
Lottie Animations from LottieFiles

Dataset from Kaggle

UI design inspired by modern dashboard styles

🛡️ Disclaimer
This tool is for educational and demonstration purposes only. It is not a replacement for professional medical diagnosis. Always consult with certified radiologists or doctors for medical advice.

