import math
import time
from constants import *

class Timer:
    def __init__(self, **kwargs):
        self.current_duration = 0
        self.pomodoros = {}
        self.pomodoros_number = 4
        self.pomodoros_completed = -1

        self.start_button = kwargs.get("start_button")
        self.canvas = kwargs.get("canvas")
        self.timer_text = kwargs.get("timer_text")
        self.check_mark = kwargs.get("check_mark")
        self.window = kwargs.get("window")
        self.status_label = kwargs.get("status_label")

        self.loop_id = None
        self.timer_on = False

    def setup_pomodoros(self):
        """Create a queue containing the durations 'Pomodoros' that will run through the countdown timer."""
        if self.current_duration < 0.1: # If countdown timer has not started
            for n in range(self.pomodoros_number + 1): # Add the required number of pomodoros to the queue
                if n < self.pomodoros_number:
                    self.pomodoros[f"{WORK_SESSION}: {n + 1}"] = [GREEN, WORK_MIN] # Dictionary format: {"Session Name: Session Number" : [Text Colour, Duration]}
                    self.pomodoros[f"{SHORT_BREAK}: {n + 1}"] = [PINK, SHORT_BREAK_MIN]
                else:
                    self.pomodoros[BREAK] = [RED, LONG_BREAK_MIN]

        self.start_handler() # Start the countdown timer

    def register_countdown(self):
        """Set the time for the countdown timer"""
        if self.current_duration == 0: # If the timer has not started or the previous timer has ended
            key_list = list(self.pomodoros.keys())
            value_list = list(self.pomodoros.values())

            self.current_duration = value_list[0][1] * 60
            self.status_label.config(text=f"{key_list[0]}", fg=value_list[0][0])

            self.pomodoros_completed += 1 # Register the number of started pomodoros
            if self.pomodoros_completed == 2:
                self.pomodoros_number -= 1
                self.pomodoros_completed = 0

            del self.pomodoros[key_list[0]] # Remove the started pomodoro from the queue

            self.window.pop_up() # Show the app window on top of all windows once a timer has started

    def counter_loop(self):
        """Countdown timer loop will take the value of the current duration in the queue and start counting it down"""
        self.canvas.itemconfig(self.timer_text, text=f"{self.format_time()}") # Update time text
        self.timer_on = True # Timer status variable
        self.loop_id = self.window.after(1000, self.counter_loop) # Create a loop timer using Tkinter library

        if self.current_duration > 0: # Decrease the time by 1 second every second
            self.current_duration -= 1
        elif self.current_duration == 0 and len(self.pomodoros) > 0: # Current timer has finished, start the next timer in the queue
            self.register_countdown()
            self.calc_pom()
        else: # The queue is empty now, reset everything
            self.reset_timer()

    def format_time(self):
        """Format the current duration from seconds to Minute:Second"""
        time_struct = time.gmtime(self.current_duration)
        return time.strftime("%M:%S", time_struct)

    def reset_timer(self):
        """Reset everything for the countdown timer including the status and the queue"""
        self.timer_on = False
        if self.loop_id is not None:
            self.window.after_cancel(self.loop_id) # Stop the loop timer
        self.current_duration = 0
        self.pomodoros_completed = -1
        self.pomodoros_number = 4
        self.pomodoros.clear()
        self.window.clear()
        self.window.pop_up()

    def start_handler(self):
        """Handle Start, Pause and Resume operations"""
        if not self.timer_on: # If timer status is PAUSED or not started yet, start the timer again
            self.start_button.config(text=PAUSE)
            self.check_mark.config(text="")
            self.register_countdown()
            self.timer_on = True
            self.counter_loop()
            self.calc_pom()
        else: # If timer is already running, pause it
            self.start_button.config(text=RESUME)
            self.check_mark.config(text=PAUSED, fg=RED)
            self.timer_on = False
            self.window.after_cancel(self.loop_id)

    def calc_pom(self):
        """Calculate the number of completed pomodoros"""
        if self.pomodoros_number < 4:
            self.check_mark.config(text=f"{POMODOROS}: {CHECK_MARK * math.floor(4-self.pomodoros_number)}", fg=GREEN)
