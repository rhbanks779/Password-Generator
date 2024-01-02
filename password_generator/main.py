import tkinter.messagebox
from tkinter import *
from tkinter import messagebox
import random
import pyperclip


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

def password_generator():
    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    # list comprehension: new_list = [new_item for item in list]

    password_letters = [random.choice(letters) for char in range(nr_letters)]
    password_symbols = [random.choice(symbols) for char in range(nr_symbols)]
    password_numbers = [random.choice(numbers) for char in range(nr_numbers)]

    password_list = password_numbers + password_symbols + password_letters
    random.shuffle(password_list)

    random.shuffle(password_list)

    password = "".join(password_list)

    password_input.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
#def success_message():
#    tkinter.messagebox.showinfo("Save Info", "Information has been saved!")

def save():
    is_ok = False
    website = website_input.get()
    email = email_input.get()
    password = password_input.get()

    if len(website) < 1 or len(email) < 1 or len(password) < 1:
        messagebox.showinfo(title="Error", message="Please enter the correct information")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"This is what you entered: \nWebsite: {website} \nEmail: {email} \nPassword: {password} \n Click OK to Save")

    if is_ok:
        with open("password_data.txt", "a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_input.delete(0, END)
            email_input.delete(0, END)
            password_input.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")

#window.minsize(width=500, height=300)
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file='logo.png')
canvas.create_image(100, 100, image=image)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_label.focus()

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
email_label.focus()

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
password_label.focus()

website_input = Entry(width=35)
website_input.grid(column=1, row=1, columnspan=2)

email_input = Entry(width=35)
email_input.grid(column=1, row=2, columnspan=2)

password_input = Entry(width=21)
password_input.grid(column=1, row=3)

generate_button = Button(text="Generate Password", command=password_generator)
generate_button.grid(column=2, row=3)

add_button = Button(text='Add', width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# pyperclip allows you to clip and paste input data, see doc for details: pypi.org/project/pyperclip
# pip install pyperclip


window.mainloop()