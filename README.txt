# Heart Disease Prediction using SVM and Flask

## 📌 Project Overview
This project is a **Heart Disease Prediction System** built using **Support Vector Machine (SVM)** with an accuracy of **98.05%**. The model takes patient data as input and predicts whether they have heart disease.

The application is deployed using **Flask**, allowing users to interact with the model through a simple web interface.

---

## 📁 Project Structure
```
heart_disease_flask/
│── app.py                # Flask application
│── index.html            # Frontend UI (HTML form for input)
│── style.css             # CSS for styling the webpage
│── svm_model.pkl         # Trained SVM model
│── svm_scaler.pkl        # Standard Scaler for input normalization
│── README.md             # Project documentation
```

---

## 🚀 How to Run the Project

### 1️⃣ Install Dependencies
Make sure you have Python installed. Then, install the required Python libraries:
```bash
pip install flask numpy joblib
```

### 2️⃣ Run the Flask Application
```bash
python app.py
```
After running, the app will be available at:
```
http://127.0.0.1:5000/
```

### 3️⃣ Expose the App to the Internet (Optional)
If you want to access the app remotely, use **Ngrok**:
```bash
ngrok http 5000
```
This will generate a public URL like:
```
https://xyz.ngrok-free.app
```
Now, anyone can access the application using this link.

---

## 🛠️ How It Works
1️⃣ **User inputs medical data** (age, cholesterol, blood pressure, etc.).  
2️⃣ **The model scales the input** using `svm_scaler.pkl`.  
3️⃣ **SVM model (`svm_model.pkl`) predicts** whether the patient has heart disease.  
4️⃣ **Result is displayed** as either `Heart Disease Detected` or `No Heart Disease`.  

---

## 🖥️ Code Breakdown

### **🔹 Flask Backend (`app.py`)**
- Loads the trained **SVM model** and **Scaler**
- Renders an HTML form (`index.html`)
- Handles **form submission & prediction logic**

### **🔹 Frontend (`index.html` + `style.css`)**
- A simple **form-based UI** for entering medical data.
- Uses **CSS** to style the form and buttons.

### **🔹 Machine Learning Model (`svm_model.pkl`)**
- A trained **SVM model** with **98.05% accuracy**.
- Uses **Standard Scaler (`svm_scaler.pkl`)** for input normalization.

---

## 📌 Example Input Data
```
Age: 63
Sex: 1 (Male)
Chest Pain Type: 3
Resting BP: 145
Cholesterol: 233
Fasting Blood Sugar: 1 (True)
Rest ECG: 0
Max Heart Rate: 150
Exercise Induced Angina: 0 (No)
Oldpeak: 2.3
Slope: 0
Number of Major Vessels: 0
Thal: 1
```

### 🔹 Expected Output
```
Prediction: Heart Disease Detected

---

## 💡 Credits
Created by **Shaz Abdulla** ✨

---

## 🤝 Contributing
Feel free to fork this project and improve it! If you find any issues, create a pull request.

🚀 Happy Coding! 🎯

