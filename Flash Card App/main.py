from tkinter import *
import pandas as pd
import random
BACKGROUND_COLOR = "#B1DDC6"
what_to_learn = {}
current_card = {}


try:
    What_to_learn = pd.read_csv("flashcard app/data/what_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("flashcard app/data/french_words.csv")
    what_to_learn = original_data.to_dict(orient="records")
else:
    what_to_learn = What_to_learn.to_dict(orient="records")


def show_french_word():
    global current_card, what_to_learn, Show_English_word
    window.after_cancel(Show_english_word_timer)  # cancel the previous timer
    current_card = random.choice(what_to_learn)
    canvas.itemconfig(canvas_bg, image=front_bg)
    canvas.itemconfig(card_label, text="French")
    canvas.itemconfig(card_word, text=current_card["French"])
    # after 3 seconds, show the English word
    show_english_word_timer = window.after(3000, show_english_word)


def show_english_word():
    canvas.itemconfig(canvas_bg, image=back_bg)
    canvas.itemconfig(card_label, text="English")
    canvas.itemconfig(card_word, text=current_card["English"])


def word_is_mastered():
    what_to_learn.remove(current_card)
    what_to_learn_df = pd.DataFrame(what_to_learn)
    what_to_learn_df.to_csv(
        "flashcard app/data/what_to_learn.csv", index=False)
    show_french_word()


window = Tk()
window.title("cards flash")
window.configure(background=BACKGROUND_COLOR)
window.config(padx=50, pady=50)

Show_english_word_timer = window.after(3000, show_english_word)


canvas = Canvas(window, width=800, height=526,
                background=BACKGROUND_COLOR, highlightthickness=0)
front_bg = PhotoImage(file="flashcard app/images/card_front.png")
back_bg = PhotoImage(file="flashcard app/images/card_back.png")
canvas_bg = canvas.create_image(412, 275, image=front_bg)
card_label = canvas.create_text(
    400, 150, text="French", font=("Ariel", 40, "italic"))
card_word = canvas.create_text(400, 263, text="partie",
                               font=("Ariel", 60, "bold"))
canvas.grid(row=0, column=0)


action_canvas = Canvas(window, width=700, height=100,
                       background=BACKGROUND_COLOR, highlightthickness=0)
wrng_icon = PhotoImage(file="flashcard app/images/wrong.png")

wrng_button = Button(action_canvas, image=wrng_icon, command=show_french_word)

wrng_button.grid(row=1, column=0, padx=200)

correct_icon = PhotoImage(file="flashcard app/images/right.png")
correct_button = Button(action_canvas, image=correct_icon,
                        command=word_is_mastered)
correct_button.grid(row=1, column=1, padx=200)
action_canvas.grid(row=1, column=0)

show_french_word()

window.mainloop() 