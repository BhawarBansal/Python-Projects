# project2_gui.py
# Random Number Guessing Game

import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, root):
        self.root = root
        self.root.title("🎲 Number Guessing Game")
        self.root.geometry("400x300")
        self.root.config(bg="#1e1e2f")

        # Game variables
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0

        # Title
        self.title_label = tk.Label(
            root,
            text="Welcome to the Number Guessing Game!",
            font=("Arial", 14, "bold"),
            fg="#f8f8f2",
            bg="#1e1e2f"
        )
        self.title_label.pack(pady=10)

        # Instructions
        self.instruction = tk.Label(
            root,
            text="I have selected a number between 1 and 100.\nCan you guess it?",
            font=("Arial", 11),
            fg="#bd93f9",
            bg="#1e1e2f"
        )
        self.instruction.pack(pady=5)

        # Entry field
        self.entry = tk.Entry(
            root,
            font=("Arial", 12),
            justify="center",
            relief="sunken",
            bd=4
        )
        self.entry.pack(pady=10, ipady=3)

        # Guess button
        self.guess_button = tk.Button(
            root,
            text="Guess",
            font=("Arial", 12, "bold"),
            bg="#50fa7b",
            fg="#1e1e2f",
            relief="raised",
            bd=6,
            command=self.check_guess
        )
        self.guess_button.pack(pady=10, ipadx=10, ipady=5)

        # Feedback label
        self.feedback = tk.Label(
            root,
            text="",
            font=("Arial", 12),
            fg="#ff79c6",
            bg="#1e1e2f"
        )
        self.feedback.pack(pady=10)

        # Reset button
        self.reset_button = tk.Button(
            root,
            text="Reset Game",
            font=("Arial", 10, "bold"),
            bg="#ff5555",
            fg="white",
            relief="raised",
            bd=5,
            command=self.reset_game
        )
        self.reset_button.pack(pady=5, ipadx=5, ipady=3)

    def check_guess(self):
        user_guess = self.entry.get()
        if not user_guess.isdigit():
            messagebox.showerror("Invalid Input", "Please enter a valid number.")
            return

        user_guess = int(user_guess)
        if user_guess <= 0:
            messagebox.showwarning("Invalid Input", "Please enter a number greater than 0.")
            return

        self.attempts += 1

        if user_guess < self.number_to_guess:
            self.feedback.config(text="⬇ Too low! Try again.")
        elif user_guess > self.number_to_guess:
            self.feedback.config(text="⬆ Too high! Try again.")
        else:
            messagebox.showinfo(
                "🎉 Congratulations!",
                f"You guessed the number {self.number_to_guess} in {self.attempts} attempts!"
            )
            self.feedback.config(text=f"Correct! 🎯 {self.number_to_guess}")
            self.guess_button.config(state="disabled")

    def reset_game(self):
        self.number_to_guess = random.randint(1, 100)
        self.attempts = 0
        self.feedback.config(text="")
        self.entry.delete(0, tk.END)
        self.guess_button.config(state="normal")


if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()
