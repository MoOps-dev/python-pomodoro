from timer_class import Timer
from ui_class import MainScreen

# ---------------------------- UI SETUP ------------------------------- #
main = MainScreen()

# ----------------------- COUNTDOWN MECHANISM ------------------------- #
timer = Timer(start_button=main.start_button, window=main, canvas=main.canvas, timer_text=main.timer_text, check_mark=main.check_mark, status_label=main.status_label)

# ------------------------ BUTTON FUNCTIONALITY ----------------------- #
main.start_button.config(command=timer.setup_pomodoros)
main.reset_button.config(command=timer.reset_timer)

main.mainloop()
