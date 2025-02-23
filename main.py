import tkinter as tk
from tkinter import messagebox
import time

# Constants
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 15
reps = 0
running = False
timer_id = None

# Timer Mechanism
def start_timer():
    global reps, running, timer_id
    if timer_id:
        window.after_cancel(timer_id)
    running = True
    reps += 1
    
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        label.config(text="Long Break")
    elif reps % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        label.config(text="Short Break")
    else:
        count_down(WORK_MIN * 60)
        label.config(text="Work")

def start_break():
    global running, timer_id
    if timer_id:
        window.after_cancel(timer_id)
    running = True
    count_down(SHORT_BREAK_MIN * 60)
    label.config(text="Break")

def reset_timer():
    global reps, running, timer_id
    if timer_id:
        window.after_cancel(timer_id)
    running = False
    canvas.itemconfig(timer_text, text="00:00")
    label.config(text="Pomodoro Timer")
    reps = 0

def count_down(count):
    global timer_id
    minutes = count // 60
    seconds = count % 60
    canvas.itemconfig(timer_text, text=f"{minutes:02d}:{seconds:02d}")
    
    if count > 0 and running:
        timer_id = window.after(1000, count_down, count - 1)
    elif count == 0:
        messagebox.showinfo("Time's Up!", "Time to switch!")
        start_timer()

# UI Setup
window = tk.Tk()
window.title("Pomodoro Timer")
window.config(padx=50, pady=20, bg="white")

label = tk.Label(window, text="Pomodoro Timer", font=("Arial", 20, "bold"), fg="black", bg="white")
label.pack()

canvas = tk.Canvas(window, width=200, height=224, bg="white", highlightthickness=0)
timer_text = canvas.create_text(100, 112, text="00:00", fill="black", font=("Arial", 35, "bold"))
canvas.pack()

start_button = tk.Button(window, text="Start", command=start_timer, font=("Arial", 12), bg="white", fg="black")
start_button.pack(side="left", padx=10, pady=10)

break_button = tk.Button(window, text="Break", command=start_break, font=("Arial", 12), bg="white", fg="black")
break_button.pack(side="left", padx=10, pady=10)

reset_button = tk.Button(window, text="Reset", command=reset_timer, font=("Arial", 12), bg="white", fg="black")
reset_button.pack(side="right", padx=10, pady=10)

window.mainloop()
