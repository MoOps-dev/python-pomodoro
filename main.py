import time
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 0.1
SHORT_BREAK_MIN = 0.1
LONG_BREAK_MIN = 0.5
timer_is_on = False
current_duration = 0
periods = {}
periods_num = 4

# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global  current_duration, timer_is_on
    timer_is_on = False
    current_duration = 0
    start_button.config(text="start")
    timer_label.config(text=f"Idle")
    canvas.itemconfig(timer_id, text=f"{format_time()}")
    periods.clear()

def pause_handler():
    global timer_is_on
    if timer_is_on:
        timer_is_on = False
        start_button.config(text="start")
    else:
        start_button.config(text="Pause")

# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global periods, timer_is_on, current_duration, periods_num

    if timer_is_on:
        pause_handler()
        return

    if current_duration < 0.1:
        for n in range(periods_num+1):
            if n < periods_num:
                periods[f"Work Session: {n+1}"] = WORK_MIN
                periods[f"Short Break: {n+1}"] = SHORT_BREAK_MIN
            else:
                periods["Break"] = LONG_BREAK_MIN
    else:
        pause_handler()
        timer_is_on = True

    start_countdown()

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def start_countdown():
    global  current_duration, timer_is_on, canvas

    if current_duration < 0.1:
        key_list = list(periods.keys())
        value_list = list(periods.values())
        current_duration = value_list[0] * 60 + 1
        timer_label.config(text=f"{key_list[0]}")
        del periods[key_list[0]]
        pause_handler()
        timer_is_on = True
        window.deiconify()
        window.wm_attributes("-topmost", False)

    while timer_is_on:
        global check_mark, periods_num

        if current_duration >= 0.1:
            current_duration -= 0.1

        if current_duration < 0.1 and len(periods) > 0:
            timer_is_on = False
            window.wm_attributes("-topmost", True)
            window.update()
            start_countdown()
        elif current_duration < 0.1 and len(periods) == 0:
            reset_timer()

        canvas.update()
        canvas.itemconfig(timer_id, text=f"{format_time()}")

        time.sleep(0.1)

def format_time():
    time_struct = time.gmtime(current_duration)
    return time.strftime("%M:%S", time_struct)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx= 10, pady=10, bg=YELLOW)
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = (screen_width - window.winfo_reqwidth()) // 2
y = (screen_height - window.winfo_reqheight()) // 2
window.geometry(f"+{x-100}+{y-100}")

timer_label = Label(text="Idle", font=(FONT_NAME, 20, "bold"), fg=GREEN, bg=YELLOW)
timer_label.grid(row=0, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_image)
timer_id = canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
canvas.grid(row=1, column=1)

start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(row=2, column=0)

reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(row=2, column=2)

check_mark = Label(text="✔", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
check_mark.grid(row=3, column=1)

window.mainloop()