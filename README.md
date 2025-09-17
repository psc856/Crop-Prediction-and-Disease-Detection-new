# 🌾 Krishi Sahaayak - AI-Powered Agriculture Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-orange.svg" alt="TensorFlow Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
</div>

<div align="center">
  <h3>🚀 Empowering farmers with cutting-edge AI technology for smarter crop management and disease detection</h3>
</div>

---

## 🌟 Live Demo

**The application is live and hosted on AWS App Runner:**

🌐 **[https://pqybsyv8bi.ap-south-1.awsapprunner.com/](https://pqybsyv8bi.ap-south-1.awsapprunner.com/)**

---

## ✨ Features

### 🔬 **Disease Detection**
- **Advanced Computer Vision**: 95%+ accuracy in crop disease identification using deep learning
- **Real-time Analysis**: Instant diagnosis from crop images with confidence scores
- **Treatment Recommendations**: Expert-curated solutions and prevention tips
- **Drag & Drop Interface**: Modern, intuitive file upload system with image preview

### 📊 **Crop Recommendation System**
- **ML-Powered Predictions**: Smart crop suggestions based on environmental parameters
- **Soil Analysis Integration**: NPK levels, pH, and nutrient requirement analysis
- **Climate Optimization**: Temperature, humidity, and rainfall pattern analysis
- **Regional Adaptation**: Localized recommendations for maximum yield potential

### 🎨 **Modern User Interface**
- **Dark/Light Theme**: Seamless theme switching with user preference persistence
- **Glassmorphism Design**: Contemporary frosted glass aesthetics with smooth animations
- **Responsive Layout**: Mobile-first design optimized for all devices
- **Interactive Elements**: Animated backgrounds with Vanta.js particle effects

---

## 🛠️ Technology Stack

### **Backend Technologies**
- **Flask** - Lightweight and flexible web framework
- **TensorFlow/Keras** - Deep learning models for disease detection
- **Scikit-learn** - Machine learning algorithms for crop recommendations
- **Pillow (PIL)** - Advanced image processing and manipulation
- **NumPy** - Numerical computing for data processing

### **Frontend Technologies**
- **HTML5/CSS3** - Modern semantic markup and styling
- **JavaScript ES6+** - Interactive user experience
- **Vanta.js** - Dynamic animated backgrounds
- **Font Awesome** - Professional icon library

### **AI/ML Models**
- **Convolutional Neural Network (CNN)** - Image classification for disease detection
- **Random Forest & SVM** - Ensemble methods for crop prediction
- **Data Preprocessing** - Image augmentation and normalization techniques

---

## 📁 Project Structure

```
krishi-sahaayak/
├── 📂 templates/
│   ├── 🏠 landing.html          # Main landing page
│   ├── 🔬 crop_disease.html     # Disease detection interface
│   └── 📊 crop_prediction.html  # Crop recommendation interface
├── 📂 static/
│   ├── 🎨 css/                  # Stylesheets and themes
│   ├── 📷 uploads/              # User uploaded images
│   └── 🖼️ assets/               # Static assets and media
├── 📂 models/
│   ├── 🧠 disease_model.h5      # Pre-trained CNN model
│   └── 📈 crop_model.pkl        # ML model for crop prediction
├── 🐍 app.py                    # Main Flask application
├── 📋 requirements.txt          # Python dependencies
├── 🐳 Dockerfile               # Container configuration
└── 📖 README.md                # Project documentation
```

---

## 🚀 Installation & Setup

### Prerequisites
- **Python 3.8+**
- **pip package manager**
- **4GB+ RAM** (for model inference)
- **Docker** (optional, for containerized deployment)

### Local Development Setup

#### 1. **Clone Repository**
```bash
git clone https://github.com/psc856/Crop-Prediction-and-Disease-Detection-new.git
cd Crop-Prediction-and-Disease-Detection-new
```

#### 2. **Create Virtual Environment**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

#### 3. **Install Dependencies**
```bash
pip install --upgrade pip
pip install -r requirements.txt
```

#### 4. **Add Pre-trained Models**
```bash
# Create models directory and add your trained models
mkdir models
# Place your models:
# - disease_model.h5 (CNN model for disease detection)
# - crop_model.pkl (ML model for crop recommendation)
```

#### 5. **Run Application**
```bash
python app.py
```

#### 6. **Access Application**
Open your browser and navigate to: `http://localhost:5000`

---

## 🐳 Docker Deployment

### Building Docker Image
```bash
# Build the Docker image
docker build -t krishi-sahaayak .

# Run the container locally
docker run -p 5000:5000 krishi-sahaayak
```

### Dockerfile Configuration
```dockerfile
FROM python:3.8-slim

WORKDIR /app
COPY . /app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

EXPOSE 5000
CMD ["python", "app.py"]
```

---

## ☁️ AWS App Runner Deployment

### Step-by-Step Deployment

#### 1. **Push to Amazon ECR**
```bash
# Create ECR repository
aws ecr create-repository --repository-name krishi-sahaayak

# Build and tag image
docker build -t krishi-sahaayak .
docker tag krishi-sahaayak:latest <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/krishi-sahaayak:latest

# Push to ECR
docker push <AWS_ACCOUNT_ID>.dkr.ecr.<REGION>.amazonaws.com/krishi-sahaayak:latest
```

#### 2. **Configure App Runner Service**
- Choose **Container Registry** → **Amazon ECR**
- Select your repository and image tag
- Configure **CPU: 1 vCPU, Memory: 2 GB**
- Set environment variables if needed
- Deploy and get your live URL

**⚠️ Note:** App Runner supports CPU-based deployment. For GPU acceleration, consider Amazon SageMaker or ECS with GPU instances.

---

## 📊 Supported Crops & Diseases

### Disease Detection Capabilities
| **Crop** | **Supported Diseases** |
|----------|------------------------|
| **Tomato** | Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus |
| **Potato** | Early Blight, Late Blight |
| **Bell Pepper** | Bacterial Spot |
| **General** | Healthy Plant Detection |

### Crop Recommendation Options
**Field Crops:** Rice, Wheat, Maize, Sugarcane, Cotton, Soybean

**Horticultural Crops:** Potato, Tomato, Apple, Banana, Grapes, Orange

**Plantation Crops:** Coffee, Coconut, Papaya

---

## 🎯 Usage Guide

### Disease Detection Workflow
1. Navigate to **"Detect Disease"** section
2. Upload crop image (JPG/PNG/WEBP format)
3. Click **"Analyze Image"** for AI processing
4. View prediction results with confidence percentage
5. Access detailed treatment recommendations

### Crop Recommendation Process
1. Go to **"Get Recommendations"** section
2. Input soil parameters (N, P, K levels, pH)
3. Enter environmental data (temperature, humidity, rainfall)
4. Submit for ML analysis
5. Receive optimal crop suggestions with rationale

---

## 🔗 API Endpoints

### Disease Detection API
```http
POST /crop_disease
Content-Type: multipart/form-data

Parameters:
- file: Image file (JPG/PNG/WEBP)

Response:
{
  "prediction": "Early Blight",
  "confidence": 95.2,
  "recommendations": {
    "treatment": "Apply fungicide...",
    "prevention": "Ensure proper drainage..."
  }
}
```

### Crop Recommendation API
```http
POST /predict
Content-Type: application/x-www-form-urlencoded

Parameters:
- Nitrogen: float
- Phosphorus: float  
- Potassium: float
- Temperature: float
- Humidity: float
- Ph: float
- Rainfall: float

Response:
{
  "recommended_crop": "Rice",
  "suitability_score": 0.92
}
```

---

## 🎨 UI/UX Features

- **Glassmorphism Design**: Modern frosted glass aesthetic with backdrop blur effects
- **Smooth Animations**: CSS transitions and JavaScript-powered interactions  
- **Responsive Layout**: Mobile-first approach with flexible grid systems
- **Theme Toggle**: Dark/light mode with system preference detection
- **Interactive Elements**: Hover effects, loading animations, and micro-interactions
- **Accessibility**: ARIA labels, keyboard navigation, and screen reader support

---


## 📞 Contact & Support

**Prashant Chauhan**
- 📧 Email: [psc856@gmail.com](mailto:psc856@gmail.com)
- 🐙 GitHub: [@psc856](https://github.com/psc856)
- 💼 LinkedIn: [Connect with me](https://linkedin.com/in/psc856)


---

<div align="center">
  <p><strong>Built with ❤️ for farmers and agriculture enthusiasts by Prashant Chauhan</strong></p>
  <p>⭐ Star this repository if you found it helpful!</p>
  
  **Last Updated:** September 2025
</div>
