import tkinter as tk
from tkinter import messagebox
import datetime
import time
import threading
import winsound


def set_alarm():
    alarm_time = entry.get().strip()
    if not alarm_time:
        messagebox.showwarning("Input Error", "Please enter time in HH:MM:SS format")
        return
    label_status.config(text=f"Alarm set for {alarm_time}")
    
    # Run alarm checking in background
    def check_alarm():
        while True:
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            clock_label.config(text=current_time)
            if current_time == alarm_time:
                messagebox.showinfo("Alarm", "Wake up! Time to get going!")
                winsound.Beep(440, 1000)
                break
            time.sleep(1)
    
    threading.Thread(target=check_alarm, daemon=True).start()


# Tkinter window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x250")
root.resizable(False, False)

# Current time display
clock_label = tk.Label(root, text="", font=("Helvetica", 32))
clock_label.pack(pady=10)

# Input box
entry = tk.Entry(root, font=("Helvetica", 18), justify="center")
entry.pack(pady=10)
entry.insert(0, "HH:MM:SS")

# Set Alarm button
btn = tk.Button(root, text="Set Alarm", font=("Helvetica", 14), command=set_alarm)
btn.pack(pady=10)

# Status label
label_status = tk.Label(root, text="", font=("Helvetica", 12))
label_status.pack(pady=10)


# Update clock continuously
def update_clock():
    now = datetime.datetime.now().strftime("%H:%M:%S")
    clock_label.config(text=now)
    root.after(1000, update_clock)

update_clock()

root.mainloop()