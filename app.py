# ============================================================
# Student Score Predictor
# Day 12 - Project Improvement
# ============================================================
# This application predicts a student's score based on the
# number of study hours using a Linear Regression model.
# ============================================================


# ============================================================
# IMPORT LIBRARIES
# ============================================================

import tkinter as tk
from tkinter import messagebox

import pandas as pd
from sklearn.linear_model import LinearRegression


# ============================================================
# LOAD DATASET
# ============================================================

# Read the student dataset from the CSV file.
data = pd.read_csv("student_scores.csv")


# ============================================================
# PREPARE DATA FOR MACHINE LEARNING
# ============================================================

# StudyHours is used as the input feature.
X = data[["StudyHours"]]

# Score is used as the target/output value.
y = data["Score"]


# ============================================================
# TRAIN LINEAR REGRESSION MODEL
# ============================================================

# Create the Linear Regression model.
model = LinearRegression()

# Train the model using the dataset.
model.fit(X, y)


# ============================================================
# APPLICATION COLORS
# ============================================================

BG_COLOR = "#0F172A"
CARD_COLOR = "#1E293B"
INPUT_COLOR = "#334155"

PRIMARY = "#8B5CF6"
PRIMARY_DARK = "#7C3AED"

WHITE = "#FFFFFF"
LIGHT_TEXT = "#CBD5E1"
MUTED_TEXT = "#94A3B8"

SUCCESS = "#22C55E"
WARNING = "#FACC15"
ORANGE = "#FB923C"


# ============================================================
# PREDICT SCORE FUNCTION
# ============================================================

def predict_score():
    """
    Get study hours from the user and predict the student's score.
    """

    try:
        # Get the value entered in the input box.
        hours = float(hours_entry.get())

        # Validate study hours.
        if hours < 0 or hours > 24:
            messagebox.showwarning(
                "Invalid Study Hours",
                "Please enter study hours between 0 and 24."
            )
            return

        # Generate prediction using the trained model.
        prediction = model.predict([[hours]])[0]

        # Keep the predicted score between 0 and 100.
        prediction = max(0, min(100, prediction))

        # Display the predicted score.
        score_label.config(
            text=f"{prediction:.1f}%",
            fg=SUCCESS
        )

        # Calculate progress bar width.
        progress_width = int(prediction * 3.2)

        # Remove the previous progress bar.
        progress_canvas.delete("progress")

        # Draw the updated progress bar.
        progress_canvas.create_rectangle(
            0,
            0,
            progress_width,
            18,
            fill=SUCCESS,
            outline="",
            tags="progress"
        )

        # Display a message based on the predicted score.
        if prediction >= 80:

            message_label.config(
                text="🌟 Excellent! Keep up the great work!",
                fg=SUCCESS
            )

        elif prediction >= 60:

            message_label.config(
                text="👍 Good job! Keep improving!",
                fg=WARNING
            )

        else:

            message_label.config(
                text="📚 Try studying a little more!",
                fg=ORANGE
            )

    except ValueError:

        # Show an error if the user enters non-numeric data.
        messagebox.showerror(
            "Invalid Input",
            "Please enter a valid number."
        )


# ============================================================
# RESET FUNCTION
# ============================================================

def reset():
    """
    Reset the application to its default state.
    """

    # Clear the input field.
    hours_entry.delete(0, tk.END)

    # Set the default study hours.
    hours_entry.insert(0, "5")

    # Reset the score display.
    score_label.config(
        text="--",
        fg=PRIMARY
    )

    # Reset the message.
    message_label.config(
        text="Enter study hours and predict your score",
        fg=MUTED_TEXT
    )

    # Clear the progress bar.
    progress_canvas.delete("progress")


# ============================================================
# MAIN APPLICATION WINDOW
# ============================================================

root = tk.Tk()

# Set the application title.
root.title("Student Score Predictor")

# Set window size.
root.geometry("700x750")

# Prevent window resizing.
root.resizable(False, False)

# Set the main background color.
root.configure(bg=BG_COLOR)


# ============================================================
# HEADER SECTION
# ============================================================

header = tk.Frame(
    root,
    bg=BG_COLOR
)

header.pack(
    fill="x",
    pady=(35, 10)
)


# Application title.
title = tk.Label(
    header,
    text="🎓 Student Score Predictor",
    font=("Segoe UI", 30, "bold"),
    bg=BG_COLOR,
    fg=WHITE
)

title.pack()


# Application subtitle.
subtitle = tk.Label(
    header,
    text="AI-powered student performance prediction",
    font=("Segoe UI", 13),
    bg=BG_COLOR,
    fg=LIGHT_TEXT
)

subtitle.pack(
    pady=(8, 0)
)


# ============================================================
# MAIN CARD
# ============================================================

card = tk.Frame(
    root,
    bg=CARD_COLOR,
    width=570,
    height=560
)

card.pack(
    padx=65,
    pady=25
)

# Prevent the frame from changing its fixed size.
card.pack_propagate(False)


# ============================================================
# INPUT SECTION
# ============================================================

input_title = tk.Label(
    card,
    text="📚  Study Hours",
    font=("Segoe UI", 16, "bold"),
    bg=CARD_COLOR,
    fg=WHITE
)

input_title.pack(
    pady=(35, 8)
)


input_hint = tk.Label(
    card,
    text="Enter how many hours you study per day",
    font=("Segoe UI", 10),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
)

input_hint.pack()


# ============================================================
# STUDY HOURS INPUT
# ============================================================

hours_entry = tk.Entry(
    card,
    font=("Segoe UI", 20, "bold"),
    width=12,
    justify="center",
    bg=INPUT_COLOR,
    fg=WHITE,
    insertbackground=WHITE,
    relief="flat",
    bd=0
)

hours_entry.pack(
    ipady=10,
    pady=18
)

# Set the default study hours.
hours_entry.insert(0, "5")


# ============================================================
# BUTTON SECTION
# ============================================================

button_frame = tk.Frame(
    card,
    bg=CARD_COLOR
)

button_frame.pack(
    pady=5
)


# ------------------------------------------------------------
# Predict Button
# ------------------------------------------------------------

predict_button = tk.Button(
    button_frame,
    text="🔮  PREDICT SCORE",
    command=predict_score,
    font=("Segoe UI", 12, "bold"),
    bg=PRIMARY,
    fg=WHITE,
    activebackground=PRIMARY_DARK,
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=30,
    pady=12
)

predict_button.pack(
    side="left",
    padx=7
)


# ------------------------------------------------------------
# Reset Button
# ------------------------------------------------------------

reset_button = tk.Button(
    button_frame,
    text="↻  RESET",
    command=reset,
    font=("Segoe UI", 12, "bold"),
    bg=INPUT_COLOR,
    fg=WHITE,
    activebackground="#475569",
    activeforeground=WHITE,
    relief="flat",
    bd=0,
    cursor="hand2",
    padx=25,
    pady=12
)

reset_button.pack(
    side="left",
    padx=7
)


# ============================================================
# RESULT SECTION
# ============================================================

result_label = tk.Label(
    card,
    text="PREDICTED SCORE",
    font=("Segoe UI", 11, "bold"),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
)

result_label.pack(
    pady=(32, 5)
)


# Display predicted score.
score_label = tk.Label(
    card,
    text="--",
    font=("Segoe UI", 48, "bold"),
    bg=CARD_COLOR,
    fg=PRIMARY
)

score_label.pack()


# ============================================================
# PROGRESS BAR
# ============================================================

progress_canvas = tk.Canvas(
    card,
    width=320,
    height=18,
    bg=INPUT_COLOR,
    highlightthickness=0
)

progress_canvas.pack(
    pady=15
)


# ============================================================
# RESULT MESSAGE
# ============================================================

message_label = tk.Label(
    card,
    text="Enter study hours and predict your score",
    font=("Segoe UI", 11),
    bg=CARD_COLOR,
    fg=MUTED_TEXT
)

message_label.pack(
    pady=5
)


# ============================================================
# MODEL INFORMATION
# ============================================================

model_info = tk.Label(
    card,
    text="🤖 Model: Linear Regression",
    font=("Segoe UI", 10, "bold"),
    bg=CARD_COLOR,
    fg=LIGHT_TEXT
)

model_info.pack(
    pady=(25, 0)
)


# ============================================================
# FOOTER
# ============================================================

footer = tk.Label(
    root,
    text="Machine Learning • Student Performance Prediction",
    font=("Segoe UI", 9),
    bg=BG_COLOR,
    fg=MUTED_TEXT
)

footer.pack(
    pady=(0, 15)
)


# ============================================================
# START APPLICATION
# ============================================================

root.mainloop()