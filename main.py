import tkinter
from math import floor

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECKMARK = "✔"
reps = 0
# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps
    reps += 1
    work_secs = WORK_MIN * 60
    short_break_secs = SHORT_BREAK_MIN * 60
    long_break_secs = LONG_BREAK_MIN * 60

    if reps % 8 ==0:
        count_down(long_break_secs)
        label.config(text="Break", fg=GREEN)
    elif reps % 2 == 0:
        count_down(short_break_secs)
        label.config(text="Break", fg=PINK)
    else:
        count_down(work_secs)
        label.config(text="Work", fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = count / 60
    count_sec = count % 60

    if  count_sec % 60 < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text= f"{floor(count_min)}:{count_sec}")
    if count > 0:
        window.after(1000, count_down, count -1)
    else:
        start_timer()

# ---------------------------- UI SETUP ------------------------------- #
window = tkinter.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)


canvas = tkinter.Canvas(width=200,height=224, bg=YELLOW, highlightthickness=0)
tomato_img = tkinter.PhotoImage(file="tomato.png")
canvas.create_image(100,112, image= tomato_img)
timer_text = canvas.create_text(100,130, text="00:00", font=(FONT_NAME, 30, "bold"), fill="white")
canvas.grid(row= 1, column= 1)

label = tkinter.Label(text="Timer", fg=GREEN, font=(FONT_NAME, 45, "normal"), bg=YELLOW)
label.grid(row= 0, column= 1)

start_button = tkinter.Button(text="Start",highlightthickness=0, height=2, command=start_timer)
start_button.grid(row= 2, column=0)

reset_button = tkinter.Button(text="Reset",highlightthickness=0, height=2)
reset_button.grid(row= 2, column=2)

checkmark = tkinter.Label(text=CHECKMARK, foreground=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
checkmark.grid(row= 3, column=1)



window.mainloop()