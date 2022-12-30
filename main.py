from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    file = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("data/french_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = file.to_dict(orient="records")



def next_card():
    global current_card, final_timer

    window.after_cancel(final_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(canvas_title, text="French", fill="black")
    canvas.itemconfig(canvas_word, text=current_card["French"], fill="black")
    canvas.itemconfig(canvas_img, image=card_front)
    final_timer = window.after(3000, sometime)


def sometime():
    canvas.itemconfig(canvas_img, image=card_back)
    canvas.itemconfig(canvas_title, text="English", fill="white")
    canvas.itemconfig(canvas_word, text=current_card["English"], fill="white")


def is_known():
    to_learn.remove(current_card)
    new = pandas.DataFrame(to_learn)
    new.to_csv("data/words_to_learn.csv", index=False)
    next_card()


window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
final_timer = window.after(3000, sometime)

card_back = PhotoImage(file="images/card_back.png")
card_front = PhotoImage(file="images/card_front.png")
canvas = Canvas(width=800, height=528)
canvas_img = canvas.create_image(400, 268, image=card_front)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas_title = canvas.create_text(400, 150, text="French", font=("ariel", 40, "italic"))
canvas_word = canvas.create_text(400, 263, text="trouve", font=("ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

next_card()
wrong_image = PhotoImage(file="images/wrong.png")
cross_button = Button(window, image=wrong_image, highlightthickness=0, command=next_card)
cross_button.grid(column=0, row=1)

right_image = PhotoImage(file="images/right.png")
tick_button = Button(window, image=right_image, highlightthickness=0, command=is_known)
tick_button.grid(column=1, row=1)











window.mainloop()
