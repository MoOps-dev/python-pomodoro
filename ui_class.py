from tkinter import *
from constants import *

class MainScreen(Tk):
    def __init__(self):
        super().__init__()
        self.title("Pomodoro Timer")
        self.config(padx=10, pady=10, bg=YELLOW)
        screen_width = self.winfo_screenwidth()
        screen_height = self.winfo_screenheight()
        x = (screen_width - self.winfo_reqwidth()) // 2
        y = (screen_height - self.winfo_reqheight()) // 2
        self.geometry(f"+{x - 100}+{y - 100}")

        self.status_label = Label(text=IDLE, font=(FONT_NAME, 20, "bold"), fg=RED, bg=YELLOW)
        self.status_label.grid(row=0, column=1)

        self.canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
        self.tomato_image = PhotoImage(file="tomato.png")
        self.canvas.create_image(100, 112, image=self.tomato_image)
        self.timer_text = self.canvas.create_text(100, 130, text="00:00", font=(FONT_NAME, 35, "bold"), fill="white")
        self.canvas.grid(row=1, column=1)

        self.start_button = Button(text=START, highlightthickness=0)
        self.start_button.grid(row=2, column=0)

        self.reset_button = Button(text=RESET, highlightthickness=0)
        self.reset_button.grid(row=2, column=2)

        self.check_mark = Label(fg=GREEN, bg=YELLOW, font=(FONT_NAME, 15, "bold"))
        self.check_mark.grid(row=3, column=1)

    def pop_up(self):
        self.wm_attributes("-topmost", True)
        self.deiconify()
        self.wm_attributes("-topmost", False)

    def clear(self):
        self.start_button.config(text=START)
        self.status_label.config(text=IDLE, fg=RED)
        self.canvas.itemconfig(self.timer_text, text="00:00")
        self.check_mark.config(text="")
