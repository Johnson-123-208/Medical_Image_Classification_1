import os
import numpy as np
import cv2
import tensorflow as tf
from tensorflow.keras import layers, models
from sklearn.model_selection import train_test_split

def load_data(data_dir):
    categories = os.listdir(data_dir)
    X, y = [], []
    for label, category in enumerate(categories):
        path = os.path.join(data_dir, category)
        for img in os.listdir(path):
            img_array = cv2.imread(os.path.join(path, img), cv2.IMREAD_GRAYSCALE)
            if img_array is not None:
                resized = cv2.resize(img_array, (100, 100))
                X.append(resized)
                y.append(label)
    return np.array(X), np.array(y)

def build_model():
    model = models.Sequential([
        layers.Input(shape=(100, 100, 1)),
        layers.Conv2D(32, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Conv2D(64, (3,3), activation='relu'),
        layers.MaxPooling2D(2,2),
        layers.Flatten(),
        layers.Dense(128, activation='relu'),
        layers.Dense(1, activation='sigmoid')
    ])
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def train():
    X, y = load_data("data/train")  # Change path based on dataset
    X = X / 255.0
    X = X.reshape(-1, 100, 100, 1)
    X_train, X_val, y_train, y_val = train_test_split(X, y, test_size=0.2)
    
    model = build_model()
    model.fit(X_train, y_train, epochs=5, validation_data=(X_val, y_val))
    model.save("model/medical_cnn.h5")
