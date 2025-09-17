import os
import numpy as np
import pickle
from flask import Flask, request, render_template, url_for
from PIL import Image
import tensorflow as tf
from werkzeug.utils import secure_filename
import requests

# ---------------------------
# Load ML models and scalers
# ---------------------------
model = pickle.load(open('model.pkl', 'rb'))
sc = pickle.load(open('standscaler.pkl', 'rb'))
ms = pickle.load(open('minmaxscaler.pkl', 'rb'))

# S3 Model Download
MODEL_PATH = "model.h5"
MODEL_S3_URL = "https://crop-recommendation-model.s3.ap-south-1.amazonaws.com/model.h5"

if not os.path.exists(MODEL_PATH):
    print("Downloading disease detection model from S3...")
    r = requests.get(MODEL_S3_URL, stream=True)
    with open(MODEL_PATH, 'wb') as f:
        for chunk in r.iter_content(chunk_size=1024*1024):
            if chunk:
                f.write(chunk)
    print("Download complete.")

disease_model = tf.keras.models.load_model(MODEL_PATH)

# ---------------------------
# Config
# ---------------------------
INPUT_SHAPE = (256, 256, 3)
CLASS_NAMES = [
    'Bell Pepper Bacterial Spot','Bell Pepper Healthy',
    'Potato Early Blight','Potato Late Blight','Potato Healthy',
    'Tomato Bacterial Spot','Tomato Early Blight','Tomato Late Blight',
    'Tomato Leaf Mold','Tomato Septoria Leaf Spot','Tomato Spider Mites',
    'Tomato Target Spot','Tomato Yellow Leaf Curl Virus','Tomato Mosaic Virus',
    'Tomato Healthy'
]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'static/uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# ---------------------------
# Routes
# ---------------------------
@app.route('/')
def landing_page():
    return render_template("landing.html")

@app.route('/index')
def index():
    return render_template("crop_prediction.html")

@app.route('/predict', methods=['POST'])
def predict():
    N = request.form['Nitrogen']
    P = request.form['Phosporus']
    K = request.form['Potassium']
    temp = request.form['Temperature']
    humidity = request.form['Humidity']
    ph = request.form['Ph']
    rainfall = request.form['Rainfall']

    feature_list = [N, P, K, temp, humidity, ph, rainfall]
    single_pred = np.array(feature_list).reshape(1, -1)

    scaled_features = ms.transform(single_pred)
    final_features = sc.transform(scaled_features)
    prediction = model.predict(final_features)

    crop_dict = {
        1: "Rice", 2: "Maize", 3: "Jute", 4: "Cotton", 5: "Coconut",
        6: "Papaya", 7: "Orange", 8: "Apple", 9: "Muskmelon",
        10: "Watermelon", 11: "Grapes", 12: "Mango", 13: "Banana",
        14: "Pomegranate", 15: "Lentil", 16: "Blackgram", 17: "Mungbean",
        18: "Mothbeans", 19: "Pigeonpeas", 20: "Kidneybeans",
        21: "Chickpea", 22: "Coffee"
    }

    if prediction[0] in crop_dict:
        crop = crop_dict[prediction[0]]
        result = f"{crop} is the best crop to be cultivated in these conditions."
    else:
        result = "Sorry, we could not determine the best crop with the provided data."

    return render_template('crop_prediction.html', result=result)

@app.route('/crop_disease', methods=['GET', 'POST'])
def crop_disease():
    if request.method == 'POST':
        file = request.files['file']
        if file:
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            # Preprocess image
            image = Image.open(file_path)
            img_batch = preprocess_image(image)

            # Predict
            predictions = disease_model.predict(img_batch)
            predicted_class = CLASS_NAMES[np.argmax(predictions)]
            confidence = np.max(predictions) * 100

            # Show image + result
            image_url = url_for('static', filename=f'uploads/{filename}')
            return render_template("crop_disease.html",
                                   image_url=image_url,
                                   prediction=predicted_class,
                                   confidence=confidence)

    return render_template("crop_disease.html", prediction=None)

# ---------------------------
# Helpers
# ---------------------------
def preprocess_image(image):
    if image.mode == 'RGBA':
        image = image.convert('RGB')
    image = image.resize((INPUT_SHAPE[1], INPUT_SHAPE[0]))
    image = np.array(image) / 255.0
    return np.expand_dims(image, axis=0)

# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":
    # For local testing
    app.run(host="0.0.0.0", port=5000, debug=True)
