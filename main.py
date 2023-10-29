from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
FRONT = "French"
BACK = "English"
random_card = {}
timer = None
try:
    words_data = pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    print("File Not found: There is no words to learn file yet")
    words_data = pandas.read_csv("data/french_words.csv")

words_list = words_data.to_dict(orient="records")


def next_card():
    global random_card
    global timer
    global words_list
    random_card = random.choice(words_list)
    word = random_card[FRONT]
    card.itemconfig(card_background, image=card_front_image)
    card.itemconfig(language_text, text=FRONT, fill="Black")
    card.itemconfig(word_text, text=word, fill="Black")
    timer = window.after(3000, flip_card)


def is_known():
    global random_card
    global words_list
    words_list.remove(random_card)
    data_frame = pandas.DataFrame(words_list)
    # print(data_frame)
    data_frame.to_csv("data/words_to_learn.csv", index=False)

    next_card()


def flip_card():
    global timer
    word = random_card[BACK]
    card.itemconfig(card_background, image=card_back_image)
    card.itemconfig(language_text, text=BACK, fill="White")
    card.itemconfig(word_text, text=word, fill="White")
    window.after_cancel(timer)


# --------------------------- UI SETUP ------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, )

card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, highlightthickness=0)
card_background = card.create_image(400, 263, image=card_front_image)
language_text = card.create_text(400, 150, text=FRONT, font=("Ariel", 40, "italic"))
word_text = card.create_text(400, 253, text="trouve", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=is_known)
right_button.grid(row=1, column=1)

next_card()

window.mainloop()
