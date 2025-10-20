from timer_class import Timer
from ui_class import MainScreen

# ---------------------------- UI SETUP ------------------------------- #
main = MainScreen() # Create the UI

# ----------------------- COUNTDOWN MECHANISM ------------------------- #
timer = Timer(start_button=main.start_button, window=main, canvas=main.canvas, timer_text=main.timer_text, check_mark=main.check_mark, status_label=main.status_label) # Create the countdown timer and pass ui elements that will be managed within it

# ------------------------ BUTTON FUNCTIONALITY ----------------------- #
main.start_button.config(command=timer.setup_pomodoros) # Set what happens when start_button is clicked
main.reset_button.config(command=timer.reset_timer) # Set what happens when reset_button is clicked

main.mainloop() # Keep the app window open
