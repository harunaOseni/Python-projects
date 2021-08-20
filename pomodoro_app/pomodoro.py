from tkinter import *
import math

window = Tk()
window.title("Pomodoro App")
window.config(padx=100, pady=50, bg="black")


canvas = Canvas(window, width=200, height=300,
                bg="black", highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 112,  image=tomato_image)
timer_count = canvas.create_text(100, 120, text="00:00", fill="white",
                                 font=("courier", 35, "bold"))
canvas.grid(row=1, column=1)

reps = 0
clock = None


def start_timer():
    global reps
    work_sec = 25 * 60
    short_break_sec = 5 * 60
    long_break_sec = 30 * 60
    reps += 1
    if reps % 2 == 0:
        timer(short_break_sec)
        timer_label.config(text="Short Break", fg="pink")
    elif reps % 8 == 0:
        timer(long_break_sec)
        timer_label.config(text="Long Break", fg="red")
    else:
        timer(work_sec)
        timer_label.config(text="Timer", fg="green")


def timer(count):
    global reps
    global clock
    # get count in minute
    count_minute = count // 60
    count_second = count % 60

    canvas.itemconfig(
        timer_count, text=f"{count_minute:02d}:{count_second:02d}")
    if count > 0:
        clock = window.after(1000, timer, count - 1)
    else:
        start_timer()
        marks = ""
        for i in range(math.floor(reps / 2)):
            marks += "✔"
        check_mark_label.config(text=f"{marks}")


def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text="00:00")
    timer_label.config(text="Timer", fg="green")
    check_mark_label.config(text="")


timer_label = Label(window, text="Timer", font=(
    "courier", 35, "bold"), fg="green", bg="black")
timer_label.grid(row=0, column=1)

start_button = Button(window, text="Start", font=(
    "courier", 20, "bold"), fg="black", bg="red", command=start_timer)
start_button.grid(row=2, column=0)


reset_button = Button(window, text="Reset", font=(
    "courier", 20, "bold"), fg="black", bg="red", command=reset_timer)

reset_button.grid(row=2, column=2)

check_mark_label = Label(fg="green",
                         bg="black", font=("courier", 20, "bold"))
check_mark_label.grid(row=3, column=1)

window.mainloop()
