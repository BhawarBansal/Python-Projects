# project1.py
# Quiz Game
import tkinter as tk
from tkinter import messagebox


# ---------------- Terminal Version ----------------
def terminal_quiz():
    print("Welcome to the Quiz Game!")
    print("You will be asked a series of questions. Try to answer them correctly!")
    playing = input("Are you ready to play? (yes/no): ").lower()
    if playing != "yes":
        print("Okay, maybe next time!")
        return
    else:
        print("Great! Let's start!")
        score = 0
        answer = input("What is the capital of France? ").lower()
        if answer == "paris":
            print("Correct! Paris is the capital of France.")
            score += 1
        else:
            print("Incorrect! The correct answer is Paris.")
        answer = input("What is 2 + 2? ")
        if answer == "4":
            print("Correct! 2 + 2 equals 4.")
            score += 1
        else:
            print("Incorrect! The correct answer is 4.")
        answer = input("What is the largest planet in our solar system? ").lower()
        if answer == "jupiter":
            print("Correct! Jupiter is the largest planet in our solar system.")
            score += 1
        else:
            print("Incorrect! The correct answer is Jupiter.")
        print(f"You answered {score} questions correctly out of 3.")
        if score == 3:
            print("Congratulations! You are a quiz master!")
        elif score == 2:
            print("Well done! You have a good knowledge of the quiz topics.")
        else:
            print("Keep trying! You can improve your quiz skills with practice.")
        print("Thanks for playing the Quiz Game! Hope you had fun!")


# ---------------- GUI Version ----------------
class QuizGameGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz Game")
        self.score = 0
        self.q_index = 0

        self.questions = [
            ("What is the capital of France?", "paris"),
            ("What is 2 + 2?", "4"),
            ("What is the largest planet in our solar system?", "jupiter")
        ]

        self.label = tk.Label(root, text="Welcome to the Quiz Game!\nClick Start to begin.", font=("Arial", 14))
        self.label.pack(pady=20)

        self.entry = tk.Entry(root, font=("Arial", 12))
        self.button = tk.Button(root, text="Submit", command=self.check_answer, state="disabled")
        self.start_button = tk.Button(root, text="Start Quiz", command=self.start_quiz)

        self.entry.pack(pady=10)
        self.button.pack(pady=5)
        self.start_button.pack(pady=10)

    def start_quiz(self):
        self.score = 0
        self.q_index = 0
        self.start_button.config(state="disabled")
        self.button.config(state="normal")
        self.show_question()

    def show_question(self):
        question, _ = self.questions[self.q_index]
        self.label.config(text=question)
        self.entry.delete(0, tk.END)

    def check_answer(self):
        user_ans = self.entry.get().lower().strip()
        _, correct_ans = self.questions[self.q_index]
        if user_ans == correct_ans:
            messagebox.showinfo("Correct!", f"Correct! {correct_ans.capitalize()} is the right answer.")
            self.score += 1
        else:
            messagebox.showerror("Incorrect!", f"Incorrect! The correct answer is {correct_ans.capitalize()}.")
        
        self.q_index += 1
        if self.q_index < len(self.questions):
            self.show_question()
        else:
            self.show_result()

    def show_result(self):
        self.button.config(state="disabled")
        self.start_button.config(state="normal")
        result = f"You answered {self.score} questions correctly out of {len(self.questions)}.\n"
        if self.score == 3:
            result += "🎉 Congratulations! You are a quiz master!"
        elif self.score == 2:
            result += "👏 Well done! You have a good knowledge of the quiz topics."
        else:
            result += "💡 Keep trying! You can improve with practice."
        messagebox.showinfo("Quiz Finished", result)


if __name__ == "__main__":
    # ---- Choose which version to run ----
    # terminal_quiz()   # uncomment this line to run terminal version
    root = tk.Tk()
    app = QuizGameGUI(root)
    root.mainloop()
