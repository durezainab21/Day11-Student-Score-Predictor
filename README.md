# 🎓 Student Score Predictor

A simple Machine Learning desktop application that predicts a student's score based on the number of study hours.

The application uses **Linear Regression** to analyze the relationship between study hours and student scores and provides an easy-to-use graphical interface built with **Tkinter**.

## ✨ Features

* 📚 Enter daily study hours
* 🤖 Predict student score using Linear Regression
* 📊 Display predicted score as a percentage
* 📈 Visual progress bar
* 💬 Performance-based feedback
* 🔄 Reset prediction
* ⚠️ Input validation
* 🎨 Modern dark-themed GUI

## 🛠️ Technologies Used

* Python
* Pandas
* Scikit-learn
* Tkinter
* Linear Regression
* CSV Dataset

## 📁 Project Structure

```text
Day11-Student-Score-Predictor/
│
├── app.py
├── student_scores.csv
├── requirements.txt
├── README.md
└── .gitignore
```

## 🧠 Machine Learning Model

The project uses **Linear Regression**.

* **Input:** Study Hours
* **Output:** Predicted Score
* **Model:** Linear Regression

The model is trained using the `student_scores.csv` dataset.

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone https://github.com/durezainab21/Day11-Student-Score-Predictor.git
```

### 2. Open the project

```bash
cd Day11-Student-Score-Predictor
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
python app.py
```

## 📊 Example

Enter the number of study hours, such as:

```text
Study Hours: 5
```

The application will calculate and display the predicted student score.

## 🎯 Learning Outcomes

Through this project, I practiced:

* Loading datasets with Pandas
* Preparing data for Machine Learning
* Training a Linear Regression model
* Making predictions with Scikit-learn
* Building a GUI using Tkinter
* Validating user input
* Organizing a Python project professionally

## 👩‍💻 Author

**Dur e Zainab**

BS Computer Science Student

---

⭐ Developed as part of my AI/ML Internship learning journey.
# 🎓 Student Score Predictor

A simple Machine Learning project that predicts a student's exam score based on the number of hours they study.

This project was developed as part of my **AI/ML Internship at Codomax Digital Solutions**. It demonstrates the basic Machine Learning workflow, including data loading, visualization, model training, prediction, and evaluation.

---

## 📌 Project Overview

The **Student Score Predictor** uses **Linear Regression** to predict a student's expected score based on their study hours.

The user enters the number of hours they studied, and the trained Machine Learning model predicts the expected exam score.

### 🎯 Objective

The main objective of this project is to understand and implement a basic supervised Machine Learning model using a real dataset.

---

## ✨ Features

- 📊 Load and analyze student score data
- 🧹 Prepare the dataset for Machine Learning
- 📈 Visualize the relationship between study hours and scores
- 🤖 Train a Linear Regression model
- 🔮 Predict student scores
- 📏 Evaluate model performance
- 💻 Simple and user-friendly prediction interface

---

## 🛠️ Technologies Used

- **Python**
- **Pandas** – Data loading and manipulation
- **NumPy** – Numerical operations
- **Matplotlib** – Data visualization
- **Scikit-learn** – Machine Learning model
- **Streamlit** – User interface
- **Jupyter Notebook** – Model development and experimentation

---

## 📂 Project Structure

```text
Student-Score-Predictor/
│
├── Student_Score_Prediction.ipynb
├── student_scores.csv
├── app.py
├── requirements.txt
├── README.md
│
└── screenshots/
    ├── prediction.png
    └── output.png