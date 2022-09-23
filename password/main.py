from tkinter import *
from random import choice, randint, shuffle
from tkinter import messagebox
import pyperclip

window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=30)

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers

    shuffle(password_list)

    password = "".join(password_list)

    password_input.delete(0, END)
    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #

def convert_input():
    entry= f"{website_input.get()} , {email_input.get()}, {password_input.get()}"
    is_ok = False

    if len(website_input.get()) == 0:
        messagebox.showinfo(title="Oh oh!", message="Looks like you forgot to enter a website.")
    elif len(email_input.get()) == 0:
        messagebox.showinfo(title="Oh oh!", message="Looks like you forgot to enter an email.")
    elif len(password_input.get()) == 0:
        messagebox.showinfo(title="Oh oh!", message="Looks like you forgot to enter a password.")
    else:
        is_ok = messagebox.askokcancel(title=f"{website_input.get()}", message=f"Email: {email_input.get()}\npassword: {password_input.get()}")

    if is_ok:
        with open("passwords.txt", mode="a") as file:
            file.write(f"\n{entry}")
        website_input.delete(0, END)
        password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

canvas = Canvas(width=200, height=200)
image_loc = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image_loc)


canvas.grid(row=0, column=1)

website_label = Label(text="Website: ")
website_label.grid(row=1, column=0, sticky="ew")

website_input = Entry(width=35)
website_input.grid(row=1, column=1, columnspan=2, sticky="ew")
website_input.focus()

email_label = Label(text="Email: ")
email_label.grid(row=2, column=0, sticky="ew")

email_input = Entry(width=35)
email_input.grid(row=2, column=1, columnspan=2, sticky="ew")
email_input.insert(0, "example@example.com")


password_label = Label(text="Password: ")
password_label.grid(row=3, column=0, sticky="ew")

password_input = Entry(width=21)
password_input.grid(row=3, column=1, sticky="ew")

generate_button = Button(text="Generate Password", command=generate_password)
generate_button.grid(row=3, column=2, sticky="ew")

add_button = Button(text="Add", width=36, command=convert_input)
add_button.grid(row=4, column=1, columnspan=2, sticky="ew")

window.mainloop()
