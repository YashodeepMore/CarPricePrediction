# Car Price Prediction Model

## Overview
This project is a **Car Price Prediction System** built using **Machine Learning**. It leverages the **Random Forest Regression** algorithm to estimate car prices based on various features like year, mileage, fuel type, and more. The model is deployed using **Flask**.

## Features
- Predicts car prices based on user inputs.
- Uses **Random Forest Regression** for accurate results.
- Simple web-based UI using **Flask**.
- Accepts input features like year, mileage, fuel type, transmission, etc.

## Technologies Used
- **Python** (pandas, numpy, scikit-learn)
- **Flask** (for API and web app)
- **HTML/CSS** (for UI)
- **Jupyter Notebook** (for model training)

## Installation
1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/car-price-prediction.git
   cd car-price-prediction
   ```
2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. **Run the Flask app:**
   ```bash
   python app.py
   ```
2. **Open your browser and go to:**
   ```
   http://127.0.0.1:5000/
   ```
3. **Enter the required car details and get the predicted price.**

## Dataset
The model is trained on a dataset containing various car attributes such as:
- **Year of Manufacture**
- **Mileage (in km)**
- **Fuel Type (Petrol/Diesel/Electric/Hybrid)**
- **Transmission Type (Manual/Automatic)**
- **Engine Size**

## Model Training
- The dataset was preprocessed (handling missing values, encoding categorical variables, feature scaling).
- The **Random Forest Regression** model was trained and evaluated.
- The trained model was saved using `joblib` for deployment.

## Deployment
- The model is served using **Flask**.
- The UI allows users to input car details and get predictions instantly.

## Contributing
Feel free to open issues or submit pull requests for improvements.

## License
This project is licensed under the **MIT License**.

## Contact
For any queries, contact **your_email@example.com** or raise an issue in the repository.
