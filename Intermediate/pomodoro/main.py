from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    reps = 0
    label.config(text="Timer", fg=GREEN)
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    ticks.config(text="")


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps +=1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60
    if reps % 8 == 0:
        count_down(long_break_secs)
        label.config(text="Break", fg=RED)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        label.config(text="Break", fg=PINK)
    elif reps % 2 == 1:
        count_down(work_secs)
        label.config(text="Work", fg=GREEN)



# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

def count_down(count):
    minutes = math.floor(count/60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count-1)
    else:
         start_timer()
         total_ticks = ""
         for x in range(math.floor(reps/2)):
             total_ticks += "✔"
         ticks.config(text=total_ticks)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro Timer")
window.config(padx=100, pady=50, bg=YELLOW)



label = Label(text="Timer", font=(FONT_NAME, 45, "bold"), bg=YELLOW, fg=GREEN)
label.grid(row=0, column=1)

canvas = Canvas(width=202, height=224, bg=YELLOW, highlightthickness=0)
image_loc = PhotoImage(file="tomato.png")
canvas.create_image(101, 112, image=image_loc)
timer_text = canvas.create_text(103, 132, text="00:00", fill="white", font=(FONT_NAME, 25, "bold"))

canvas.grid(row=1, column=1)

start_button = Button(text="Start", command=start_timer)
start_button.grid(row=2, column=0)


ticks = Label(text="", font=(FONT_NAME, 20, "bold"), bg=YELLOW, fg=GREEN)
ticks.grid(row=3, column=1)

reset_button = Button(text="Reset", command=reset_timer)
reset_button.grid(row=2, column=2)

window.mainloop()
