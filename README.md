# Medical_Image_Classification_1
# 🧠 Medical Image Classification - Pneumonia Detection

This project uses a Convolutional Neural Network (CNN) to detect **Pneumonia** from chest X-ray images. Built in Python with TensorFlow/Keras, it automates dataset download from **Kaggle**, trains a CNN model, and can be easily extended for deployment or experimentation.

---

## 🚀 Features

- 🧠 CNN model for early disease detection  
- 📦 Auto-downloads dataset via Kaggle API  
- 📊 Performance metrics and visualizations  
- 🎨 Clean modular code (VSCode-friendly)  
- 💻 Ready for deployment & GitHub integration  

---

## 📊 Dataset

We're using the [Chest X-ray Pneumonia dataset](https://www.kaggle.com/datasets/paultimothymooney/chest-xray-pneumonia) from Kaggle. It contains images of normal and pneumonia-affected lungs, categorized into training, testing, and validation folders.

Due to GitHub's size limits, the dataset is **not included in this repo**. But no worries — it will be automatically downloaded when you run the training script!

---

## 🔧 Setup Instructions

### 1️⃣ Clone the Repo

```bash
git clone https://github.com/<your-username>/medical-image-classification.git
cd medical-image-classification
2️⃣ Install Dependencies
bash
Copy
Edit
pip install -r requirements.txt
3️⃣ Setup Kaggle API
Go to your Kaggle Account Settings.

Click Create New API Token – this downloads kaggle.json.

Place kaggle.json in this path:

makefile
Copy
Edit
Windows:    C:\Users\<YourUsername>\.kaggle\kaggle.json  
Linux/Mac:  ~/.kaggle/kaggle.json
✅ Make sure the file is named exactly kaggle.json.

🏁 Run the Training Script
bash
Copy
Edit
python model/train_model.py
This will:

🔁 Check if dataset is present

⬇️ If not, download it from Kaggle automatically

🧠 Train the CNN model on the dataset

📈 Print metrics and save model outputs

📁 Project Structure
bash
Copy
Edit
medical-image-classification/
│
├── data/                  # (Auto-created) Dataset download folder
├── model/
│   └── train_model.py     # Main training script
├── utils/
│   └── helpers.py         # Helper functions (e.g., Kaggle dataset download)
├── .gitignore             # Ignores data/ and kaggle.json
└── README.md              # You're here!
🔒 .gitignore
Make sure your .gitignore includes:

graphql
Copy
Edit
# Dataset and API key
data/
.kaggle/
📬 Credits
Dataset by Paul Timothy Mooney

Built with ❤️ using TensorFlow & Python

🧠 Future Plans
🔬 Model accuracy boosting

📱 Web interface (Streamlit or Flask)

🌐 Deploy model to the cloud

📎 License
Open source under MIT License.

yaml
Copy
Edit

---