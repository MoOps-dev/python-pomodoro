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
        if self.current_duration < 0.1:
            for n in range(self.pomodoros_number + 1):
                if n < self.pomodoros_number:
                    self.pomodoros[f"{WORK_SESSION}: {n + 1}"] = [GREEN, WORK_MIN]
                    self.pomodoros[f"{SHORT_BREAK}: {n + 1}"] = [PINK, SHORT_BREAK_MIN]
                else:
                    self.pomodoros[BREAK] = [RED, LONG_BREAK_MIN]

        self.start_handler()

    def register_countdown(self):
        if self.current_duration == 0:
            key_list = list(self.pomodoros.keys())
            value_list = list(self.pomodoros.values())

            self.current_duration = value_list[0][1] * 60
            self.status_label.config(text=f"{key_list[0]}", fg=value_list[0][0])

            self.pomodoros_completed += 1
            if self.pomodoros_completed == 2:
                self.pomodoros_number -= 1
                self.pomodoros_completed = 0

            del self.pomodoros[key_list[0]]

            self.window.pop_up()

    def counter_loop(self):
        self.canvas.itemconfig(self.timer_text, text=f"{self.format_time()}")
        self.timer_on = True
        self.loop_id = self.window.after(1000, self.counter_loop)

        if self.current_duration > 0:
            self.current_duration -= 1
        elif self.current_duration == 0 and len(self.pomodoros) > 0:
            self.register_countdown()
            self.calc_pom()
        else:
            self.reset_timer()

    def format_time(self):
        time_struct = time.gmtime(self.current_duration)
        return time.strftime("%M:%S", time_struct)

    def reset_timer(self):
        self.timer_on = False
        self.window.after_cancel(self.loop_id)
        self.current_duration = 0
        self.pomodoros_completed = -1
        self.pomodoros_number = 4
        self.pomodoros.clear()
        self.window.clear()
        self.window.pop_up()

    def start_handler(self):
        if not self.timer_on:
            self.start_button.config(text=PAUSE)
            self.check_mark.config(text="")
            self.register_countdown()
            self.timer_on = True
            self.counter_loop()
            self.calc_pom()
        else:
            self.start_button.config(text=RESUME)
            self.check_mark.config(text=PAUSED, fg=RED)
            self.timer_on = False
            self.window.after_cancel(self.loop_id)

    def calc_pom(self):
        if self.pomodoros_number < 4:
            self.check_mark.config(text=f"{POMODOROS}: {CHECK_MARK * math.floor(4-self.pomodoros_number)}", fg=GREEN)
