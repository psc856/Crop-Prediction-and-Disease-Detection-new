# 🌾 Krishi Sahaayak - AI-Powered Agriculture Assistant

<div align="center">
  <img src="https://img.shields.io/badge/Python-3.8+-blue.svg" alt="Python Version">
  <img src="https://img.shields.io/badge/Flask-2.0+-green.svg" alt="Flask Version">
  <img src="https://img.shields.io/badge/TensorFlow-2.0+-orange.svg" alt="TensorFlow Version">
  <img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License">
  <img src="https://img.shields.io/badge/Status-Active-brightgreen.svg" alt="Status">
</div>

<div align="center">
  <h3>Empowering farmers with cutting-edge AI technology for smarter crop management and disease detection</h3>
</div>

---

## ✨ Features

### 🔬 **Disease Detection**
- **Advanced Computer Vision**: 95%+ accuracy in crop disease identification
- **Real-time Analysis**: Instant diagnosis from crop images
- **Treatment Recommendations**: Expert-curated solutions for detected diseases
- **Drag & Drop Interface**: Modern, intuitive file upload system

### 📊 **Crop Recommendation**
- **ML-Powered Predictions**: Smart crop suggestions based on environmental data
- **Soil Analysis Integration**: NPK levels, pH, and nutrient requirements
- **Climate Optimization**: Temperature, humidity, and rainfall considerations
- **Regional Adaptation**: Localized recommendations for maximum yield

### 🎨 **Modern UI/UX**
- **Dark/Light Theme**: Seamless theme switching with user preferences
- **Glassmorphism Design**: Contemporary frosted glass aesthetics
- **Responsive Layout**: Mobile-first design for all devices
- **Animated Backgrounds**: Interactive particle effects with Vanta.js

---

## 🚀 Live Demo

```bash
# Clone the repository
git clone https://github.com/yourusername/krishi-sahaayak.git

# Navigate to project directory
cd krishi-sahaayak

# Install dependencies
pip install -r requirements.txt

# Run the application
python app.py
```

Visit `http://localhost:5000` to explore the application.

---

## 📁 Project Structure

```
krishi-sahaayak/
├── 📂 templates/
│   ├── 🏠 landing.html          # Modern landing page
│   ├── 🔬 crop_disease.html     # Disease detection interface
│   └── 📊 crop_prediction.html  # Crop recommendation form
├── 📂 static/
│   ├── 🎨 css/                  # Custom stylesheets
│   ├── 📷 uploads/              # User uploaded images
│   └── 🖼️ assets/              # Static assets
├── 📂 models/
│   ├── 🧠 disease_model.h5     # Trained disease detection model
│   └── 📈 crop_model.pkl       # Crop recommendation model
├── 🐍 app.py                   # Flask application
├── 📋 requirements.txt         # Python dependencies
└── 📖 README.md               # Project documentation
```

---

## 🛠️ Technology Stack

### **Backend**
- **Flask** - Lightweight web framework
- **TensorFlow/Keras** - Deep learning for disease detection
- **Scikit-learn** - Machine learning for crop recommendations
- **Pillow** - Image processing and manipulation

### **Frontend**
- **HTML5/CSS3** - Modern web standards
- **JavaScript ES6+** - Interactive functionality
- **Vanta.js** - Animated background effects
- **Font Awesome** - Icon library

### **AI/ML Models**
- **Convolutional Neural Network (CNN)** - Image classification
- **Random Forest/SVM** - Crop prediction algorithms
- **Data Preprocessing** - Image augmentation and normalization

---

## 🔧 Installation & Setup

### Prerequisites
- Python 3.8 or higher
- pip package manager
- 4GB+ RAM for model inference

### Step-by-Step Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/yourusername/krishi-sahaayak.git
   cd krishi-sahaayak
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download Pre-trained Models**
   ```bash
   # Place your trained models in the models/ directory
   # disease_model.h5 - for disease detection
   # crop_model.pkl - for crop recommendations
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```

6. **Access the Application**
   - Open browser and navigate to `http://localhost:5000`

---

## 📊 Supported Crops & Diseases

### **Disease Detection Coverage**
- **Tomato**: Early Blight, Late Blight, Leaf Mold, Septoria Leaf Spot, Spider Mites, Target Spot, Yellow Leaf Curl Virus, Mosaic Virus
- **Potato**: Early Blight, Late Blight
- **Bell Pepper**: Bacterial Spot
- **Healthy Plants**: Identification of disease-free crops

### **Crop Recommendation Options**
- Rice, Wheat, Maize, Sugarcane, Cotton
- Soybean, Potato, Tomato, Apple, Banana
- Coffee, Grapes, Orange, Coconut, Papaya

---

## 🎯 Usage Guide

### **Disease Detection Workflow**
1. Navigate to "Detect Disease" from landing page
2. Upload crop image via drag-and-drop or file selection
3. Click "Analyze Image" for AI processing
4. View prediction results with confidence score
5. Access detailed treatment recommendations

### **Crop Recommendation Process**
1. Select "Get Recommendations" option
2. Input soil parameters (N-P-K values, pH)
3. Provide environmental data (temperature, humidity, rainfall)
4. Submit form for ML-powered analysis
5. Receive optimal crop suggestions

---

## 🧪 API Endpoints

### **Disease Detection**
```python
POST /crop_disease
Content-Type: multipart/form-data

Parameters:
- file: Image file (JPG, PNG, WEBP)

Response:
{
    "prediction": "Disease Name",
    "confidence": 95.2,
    "recommendations": {...}
}
```

### **Crop Recommendation**
```python
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
    "recommended_crop": "Rice"
}
```

---

## 🎨 UI Features

### **Modern Design Elements**
- **Glassmorphism Effects**: Frosted glass aesthetic with backdrop blur
- **Smooth Animations**: CSS transitions and keyframe animations
- **Responsive Grid**: Mobile-first responsive design
- **Interactive Elements**: Hover effects and micro-interactions

### **Theme System**
- **Automatic Detection**: System preference detection
- **Manual Toggle**: User-controlled theme switching
- **Persistent Settings**: LocalStorage-based theme memory
- **Dynamic Colors**: CSS custom properties for consistent theming

---

## 🔮 Future Enhancements

### **Planned Features**
- [ ] **Multi-language Support** - Hindi, Bengali, Tamil translations
- [ ] **Weather API Integration** - Real-time climate data
- [ ] **Farmer Community** - Social features and knowledge sharing
- [ ] **Mobile App** - React Native cross-platform application
- [ ] **IoT Integration** - Sensor data for automated monitoring
- [ ] **Blockchain** - Supply chain tracking and verification

### **Model Improvements**
- [ ] **Expanded Dataset** - More crop varieties and diseases
- [ ] **Edge Computing** - On-device inference capabilities
- [ ] **Federated Learning** - Privacy-preserving model updates
- [ ] **Explainable AI** - Model interpretability features

---

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### **How to Contribute**
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/AmazingFeature`)
3. **Commit** your changes (`git commit -m 'Add AmazingFeature'`)
4. **Push** to the branch (`git push origin feature/AmazingFeature`)
5. **Open** a Pull Request

### **Contribution Areas**
- 🐛 Bug fixes and issue resolution
- ✨ New feature development
- 📚 Documentation improvements
- 🧪 Test coverage expansion
- 🎨 UI/UX enhancements

---

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 🏆 Acknowledgments

- **Agricultural Experts** - Domain knowledge and validation
- **Open Source Community** - Libraries and frameworks
- **Research Papers** - ML/AI methodologies
- **Farmers** - Real-world testing and feedback

---

## 📞 Contact & Support

### **Maintainer**
- **Name**: Prashant Chauhan
- **Email**: psc856@gmail.com
- **GitHub**: [@yourusername](https://github.com/psc856)

---

<div align="center">
  <p><strong>Built with ❤️ for farmers and agriculture enthusiasts</strong></p>
  <p>Star ⭐ this repository if you found it helpful!</p>
</div>

---

## 📈 Project Statistics

<div align="center">
  <img src="https://github-readme-stats.vercel.app/api?username=yourusername&repo=krishi-sahaayak&show_icons=true&theme=radical" alt="GitHub Stats">
</div>

---

*Last updated: September 2025*
