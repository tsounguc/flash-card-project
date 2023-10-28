from tkinter import *
import pandas
import random

BACKGROUND_COLOR = "#B1DDC6"
words_data = pandas.read_csv("data/french_words.csv")

french_words = words_data["French"].to_list()
print(french_words)
def pick_random_word():
    random_word = random.choice(french_words)
    card.itemconfig(front_word_text, text=random_word)

# --------------------------- UI SETUP ------------------------- #
window = Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR, )

card_back_image = PhotoImage(file="images/card_back.png")
card_front_image = PhotoImage(file="images/card_front.png")
card = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightcolor=BACKGROUND_COLOR, highlightthickness=0)
card.create_image(400, 263, image=card_front_image)
front_language_text = card.create_text(400, 150, text="French", font=("Ariel", 40, "italic"))
front_word_text = card.create_text(400, 253, text="trouve", font=("Ariel", 60, "bold"))
card.grid(row=0, column=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong_button = Button(image=wrong_image, highlightthickness=0, command=pick_random_word)
wrong_button.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right_button = Button(image=right_image, highlightthickness=0, command=pick_random_word)
right_button.grid(row=1, column=1)



window.mainloop()
