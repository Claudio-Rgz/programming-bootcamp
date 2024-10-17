from tkinter import *
from tkinter import messagebox
from random import randint, choice, shuffle
from pyperclip import copy
import json


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
    website = website_entry.get()
    email = email_entry.get()
    password = password_display.get()
    new_data = {
        website.lower(): {
            "email": email.lower(),
            "password": password,
        }
    }

    if len(website) == 0 or len(password) == 0:
        blank_entry = messagebox.showerror(
            "Missing Information", "Please don't leave any fields empty!"
        )
    else:
        try:
            with open("database.json", "r") as f:
                # Read the information from our database
                data = json.load(f)
                data.update(new_data)
        except FileNotFoundError:
            with open("database.json", "w") as f:
                json.dump(new_data, f, indent=4)
        else:
            with open("database.json", "w") as f:
                json.dump(data, f, indent=4)
        finally:
            website_entry.delete(0, "end")
            password_display.delete(0, "end")


# ------------------------- SEARCH PASSWORD ---------------------------- #
def search():
    website = website_entry.get()
    website = website.lower()

    if len(website) == 0:
        messagebox.showerror(
            "Missing Information", "Please don't leave the website field empty!"
        )
    else:
        try:
            with open("database.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            messagebox.showerror(
                title="Error",
                message="No DataFile found.",
            )
        else:
            try:
                email = data[website]["email"]
                password = data[website]["password"]

                copy(password)

                messagebox.showinfo(
                    title="Information",
                    message=f"Website: {website.title()}\nEmail: {email}\nPassword: {password}",
                )
            except KeyError:
                messagebox.showerror(
                    title="Error",
                    message="There's no saved password for that webpage.",
                )


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
website_txt = Label(
    text="Website:", pady=5, font=("Arial", 8, "normal"), background="white"
)
website_txt.grid(column=0, row=1)

# Website entry
website_entry = Entry()
website_entry.focus()
website_entry.grid(column=1, row=1, sticky="EW")

# Search button
search_button = Button(
    text="Search",
    width=16,
    # pady=5,
    font=("Arial", 8, "normal"),
    background="white",
    command=search,
)
search_button.grid(column=2, row=1)

# Email Label
email_txt = Label(
    text="Email/Username:", pady=5, font=("Arial", 8, "normal"), background="white"
)
email_txt.grid(column=0, row=2)

# Email entry
email_entry = Entry()
email_entry.insert(0, "rgz.claudio@gmail.com")
email_entry.grid(column=1, row=2, columnspan=2, sticky="EW")

# Password text
password_txt = Label(
    text="Password:", pady=5, font=("Arial", 8, "normal"), background="white"
)
password_txt.grid(column=0, row=3)

# Password display
password_display = Entry()
password_display.grid(column=1, row=3, sticky="EW")

# Password generator button
password_button = Button(
    text="Generate Password",
    width=16,
    # pady=5,
    font=("Arial", 8, "normal"),
    background="white",
    command=generate_password,
)
password_button.grid(column=2, row=3)

# Add button
add_button = Button(
    text="Add",
    # pady=5,
    font=("Arial", 8, "normal"),
    background="white",
    width=50,
    command=save,
)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()
