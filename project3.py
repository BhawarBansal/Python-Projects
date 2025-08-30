import tkinter as tk
import random

# -------------------- Backend Functions --------------------
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "paper" and computer_choice == "rock") or \
         (user_choice == "scissors" and computer_choice == "paper"):
        return "user"
    else:
        return "computer"

# -------------------- Score variables --------------------
user_score = 0
comp_score = 0

# -------------------- GUI Functions --------------------
def play(user_choice):
    global user_score, comp_score
    computer_choice = get_computer_choice()
    winner = determine_winner(user_choice, computer_choice)

    if winner == "tie":
        result_label.config(text=f"Draw! Both chose {user_choice}", fg="blue")
    elif winner == "user":
        user_score += 1
        result_label.config(text=f"You Win! {user_choice} beats {computer_choice}", fg="green")
    else:
        comp_score += 1
        result_label.config(text=f"You Lose! {computer_choice} beats {user_choice}", fg="red")

    # update labels
    user_label.config(text=f"Your Choice: {user_choice}")
    comp_label.config(text=f"Computer's Choice: {computer_choice}")
    score_label.config(text=f"You: {user_score}   |   Computer: {comp_score}")

def reset_scores():
    global user_score, comp_score
    user_score = 0
    comp_score = 0
    score_label.config(text=f"You: {user_score}   |   Computer: {comp_score}")
    result_label.config(text="Scores reset. Make your move!", fg="white")
    user_label.config(text="Your Choice: ")
    comp_label.config(text="Computer's Choice: ")

# -------------------- Main GUI Window --------------------
root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.geometry("420x380")
root.config(bg="#2c3e50")

title_label = tk.Label(root, text="Rock Paper Scissors", font=("Arial", 18, "bold"), bg="#2c3e50", fg="white")
title_label.pack(pady=8)

# Choice labels
user_label = tk.Label(root, text="Your Choice: ", font=("Arial", 12), bg="#2c3e50", fg="white")
user_label.pack(pady=2)

comp_label = tk.Label(root, text="Computer's Choice: ", font=("Arial", 12), bg="#2c3e50", fg="white")
comp_label.pack(pady=2)

# Result label
result_label = tk.Label(root, text="Result: ", font=("Arial", 14, "bold"), bg="#2c3e50", fg="yellow")
result_label.pack(pady=8)

# Scoreboard
score_label = tk.Label(root, text=f"You: {user_score}   |   Computer: {comp_score}",
                       font=("Arial", 14, "bold"), bg="#2c3e50", fg="lightgreen")
score_label.pack(pady=6)

# Buttons
btn_frame = tk.Frame(root, bg="#2c3e50")
btn_frame.pack(pady=12)

rock_btn = tk.Button(btn_frame, text="✊ Rock", font=("Arial", 14, "bold"),
                     bg="gray", fg="white", width=12, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=8, pady=8)

paper_btn = tk.Button(btn_frame, text="✋ Paper", font=("Arial", 14, "bold"),
                      bg="white", fg="black", width=12, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=8, pady=8)

scissors_btn = tk.Button(btn_frame, text="✌️ Scissors", font=("Arial", 14, "bold"),
                         bg="red", fg="white", width=12, command=lambda: play("scissors"))
scissors_btn.grid(row=1, column=0, columnspan=2, pady=8)

# Reset button
reset_btn = tk.Button(root, text="Reset Scores", font=("Arial", 10, "bold"),
                      bg="#34495e", fg="white", command=reset_scores)
reset_btn.pack(pady=6)

root.mainloop()