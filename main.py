import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #

# https://colorhunt.co/
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
REPS = 0
TIMER = None


# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(TIMER)
    canvas.itemconfig(timer_text, text="00:00")
    timer_label.config(text="Timer", fg=GREEN)
    check_label.config(text="")
    global REPS
    REPS = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():

    global REPS
    REPS += 1

    if REPS % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    elif REPS % 2 == 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
    else:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    global TIMER
    count_minutes = math.floor(count / 60)
    count_seconds = count % 60
    if count_seconds < 10:
        count_seconds = f"0{count_seconds}"

    canvas.itemconfig(timer_text, text=f"{count_minutes}:{count_seconds}")
    if count > 0:
        TIMER = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        for _ in range(math.floor(REPS/2)):
            mark += "✔"
        check_label.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 30, "bold"))
canvas.grid(column=1, row=1)

timer_label = Label(text="Timer")
timer_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 50, "bold"))
timer_label.grid(column=1, row=0)

start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row=2)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(column=2, row=2)

check = "✔"

check_label = Label()
check_label.config(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 14, "bold"))
check_label.grid(column=1, row=3)
window.mainloop()
