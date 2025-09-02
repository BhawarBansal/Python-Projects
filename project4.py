import tkinter as tk
from tkinter import messagebox

# Game data (same dictionary logic)
locations = {
    "forest": {
        "desc": "You are in a dark forest. Paths lead north and east.",
        "options": {"north": "cave", "east": "river"}
    },
    "cave": {
        "desc": "You enter a cave. It's cold and dark. There's a chest here.",
        "options": {"open chest": "treasure", "south": "forest"}
    },
    "river": {
        "desc": "You stand by a fast flowing river. There's a bridge to the north.",
        "options": {"north": "waterfall", "west": "forest"}
    },
    "waterfall": {
        "desc": "Behind the waterfall, you discover a hidden passage!",
        "options": {"enter": "treasure", "south": "river"}
    },
    "treasure": {
        "desc": "🎉 Congratulations! You found the hidden treasure and won the game! 🎉",
        "options": {}
    }
}

# Main Game Class
class AdventureGame:
    def __init__(self, root):   # ✅ Constructor ka naam __init_ hona chahiye
        self.root = root
        self.root.title("Adventure Game")
        self.root.geometry("700x500")

        # Jungle theme background
        self.canvas = tk.Canvas(root, width=700, height=500, bg="#013220")  # Dark jungle green
        self.canvas.pack(fill="both", expand=True)

        # Frame for text + buttons
        self.frame = tk.Frame(self.canvas, bg="#013220")
        self.frame.place(relx=0.5, rely=0.5, anchor="center")

        # Game description label
        self.text = tk.Label(self.frame, text="", wraplength=600, font=("Georgia", 14), fg="gold", bg="#013220")
        self.text.pack(pady=20)

        # Buttons frame
        self.buttons_frame = tk.Frame(self.frame, bg="#013220")
        self.buttons_frame.pack()

        # Start location
        self.current_location = "forest"
        self.update_scene()

    def update_scene(self):
        # Clear old buttons
        for widget in self.buttons_frame.winfo_children():
            widget.destroy()

        # Update text
        loc = locations[self.current_location]
        self.text.config(text=loc["desc"])

        # Add option buttons
        for action, new_loc in loc["options"].items():
            btn = tk.Button(self.buttons_frame, text=action.title(),
                            command=lambda loc=new_loc: self.move(loc),
                            font=("Arial", 12), bg="gold", fg="black", width=20)
            btn.pack(pady=5)

        # If no options (game won)
        if not loc["options"]:
            tk.Button(self.buttons_frame, text="Exit Game", command=self.root.quit,
                      font=("Arial", 12), bg="red", fg="white", width=20).pack(pady=10)

    def move(self, new_location):
        self.current_location = new_location
        self.update_scene()


# Run game
if __name__ == "__main__":   # ✅ sahi likhna yaha
    root = tk.Tk()
    game = AdventureGame(root)
    root.mainloop()