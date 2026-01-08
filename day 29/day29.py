# PASSWORD MANAGER
import random
import string
from tkinter import *
from tkinter import messagebox
import pyperclip

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def password_generator():
    password = ''.join(random.choice(string.ascii_lowercase+string.ascii_uppercase + string.digits) for _ in range(12))
    pass_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    
    website = website_entry.get()
    email = email_entry.get()
    password = pass_entry.get()
    
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Please make sure you haven't left any field empty.")
    else:    
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered : \n\nEmail: {email} \nPassword: {password} \n\nIs it OK to save?")
    
        if is_ok:
            with open("password-data.txt", "a") as data_file:
                data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0, END)
                pass_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
EMAIL_FIELD = "email@example.com"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="./day 29/logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

pass_label = Label(text="Password:")
pass_label.grid(column=0,row=3)

website_entry = Entry(width=38)
website_entry.grid(column=1, row=1, columnspan=2)
website_entry.focus()

email_entry = Entry(width=38)
email_entry.grid(column=1, row=2, columnspan=2)
email_entry.insert(0, EMAIL_FIELD)

pass_entry = Entry(width=28)
pass_entry.grid(column=1, row=3)

pass_generator = Button(text="Generate Password", command=password_generator)
pass_generator.grid(column=2, row=3)

add_button = Button(text="Add",width=36, command=save)
add_button.grid(column=1, row=4, columnspan=2, pady=8)

window.mainloop()