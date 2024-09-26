from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = [
        "a",
        "b",
        "c",
        "d",
        "e",
        "f",
        "g",
        "h",
        "i",
        "j",
        "k",
        "l",
        "m",
        "n",
        "o",
        "p",
        "q",
        "r",
        "s",
        "t",
        "u",
        "v",
        "w",
        "x",
        "y",
        "z",
        "A",
        "B",
        "C",
        "D",
        "E",
        "F",
        "G",
        "H",
        "I",
        "J",
        "K",
        "L",
        "M",
        "N",
        "O",
        "P",
        "Q",
        "R",
        "S",
        "T",
        "U",
        "V",
        "W",
        "X",
        "Y",
        "Z",
    ]

    numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]

    symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

    letters_list = [choice(letters) for _ in range(randint(8, 10))]
    symbols_list = [choice(symbols) for _ in range(randint(2, 4))]
    numbers_list = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = letters_list + symbols_list + numbers_list

    shuffle(password_list)

    password = "".join(password_list)

    copy(password)
    password_display.insert(string=password, index=0)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    if len(website_entry.get()) == 0 or len(password_display.get()) == 0:
        blank_entry = messagebox.showerror(
            "Missing Information", "Please don't leave any fields empty!"
        )
    else:
        confirmation = messagebox.askyesno(
            title=f"{website_entry.get()}",
            message=f"These are the the details entered: \nEmail: {email_entry.get()}"
            f"\nPassword: {password_display.get()} \nIs it ok to save?",
        )
        if confirmation == True:
            with open("database.txt", "a") as f:
                f.write(
                    f"{website_entry.get()} | {email_entry.get()} | {password_display.get()}\n"
                )

            website_entry.delete(0, "end")
            password_display.delete(0, "end")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Lock image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="assets/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Website Label
website_txt = Label(text="Website:", font=("Arial", 8, "normal"), background="white")
website_txt.grid(column=0, row=1)

# Website entry
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2, sticky="EW")

# Email Label
email_txt = Label(
    text="Email/Username:", font=("Arial", 8, "normal"), background="white"
)
email_txt.grid(column=0, row=2)

# Email entry
email_entry = Entry()
email_entry.insert(0, "rgz.claudio@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password text
password_txt = Label(text="Password:", font=("Arial", 8, "normal"), background="white")
password_txt.grid(column=0, row=3)

# Password display
password_display = Entry()
password_display.grid(column=1, row=3, sticky="EW")

# Password generator button
password_button = Button(
    text="Generate Password",
    font=("Arial", 8, "normal"),
    background="white",
    command=generate_password,
)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(
    text="Add", font=("Arial", 8, "normal"), background="white", width=50, command=save
)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
