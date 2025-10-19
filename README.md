# Python Pomodoro
The Pomodoro Technique is a time management method that uses a timer to break work into 25-minute intervals, 
called "pomodoros," separated by 5-minute breaks. After four pomodoros, 
a longer 15-30 minute break is taken. This approach is designed to improve focus by reducing distractions, 
prevent burnout, and increase motivation.

## Language practices within this project:
- Tkinter library
- GUI with Tkinter
- OOP
- Keyword arguments with '**kwargs'
- Lists, dictionaries, loops
- Time formatting:

```` python
    def format_time(self):
        time_struct = time.gmtime(self.current_duration)
        return time.strftime("%M:%S", time_struct)
````
## App Features:
- 4 pomodoro timers followed in the pomodoro technique: 25-minute work session followed by 5-minute short break
- Long break of 15 minutes after completing 4 pomodoros
- Start - Pause - Resume buttons
- Reset button for resetting the pomodoros
- App window will pop on top of all windows after completing each countdown
- Pomodoro count label showing the number of the completed pomodoros
- Current status label (Work Session - Short Break - Break)

## App Preview:

![Python Pomodoro](https://media0.giphy.com/media/v1.Y2lkPTc5MGI3NjExY3h3cmNsamQwaDk4YjI0aWEzeGk2dHZ6bGNjMWdxdnpsY24wcnBwciZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/qsNfDCv3pCtb0kL0Rg/giphy.gif)