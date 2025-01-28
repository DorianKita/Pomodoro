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

# ---------------------------- TIMER RESET ------------------------------- # 

# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    count_down(5 * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):

    count_min = count / 60
    count_sec = count % 60
    print(count_min, count_sec)
    canvas.itemconfig(timer_text, text= f"{floor(count_min)}:{floor(count_sec)}")
    if count > 0:
        window.after(1000, count_down, count -1)

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