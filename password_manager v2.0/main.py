# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
from tkinter import messagebox
from tkinter import *
import random
import pyperclip
import json


def generare_password():
    global password_entry
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
               'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    letters = [random.choice(letters) for i in range(nr_letters)]
    numbers = [random.choice(numbers) for i in range(nr_numbers)]
    symbols = [random.choice(symbols) for i in range(nr_symbols)]
    password = []
    password.extend(letters)
    password.extend(numbers)
    password.extend(symbols)
    random.shuffle(password)
    generated_password = ''.join(password)
    password_entry.insert(0, generated_password)
    pyperclip.copy(generated_password)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def save():
    global website_entry, email_username_entry, password_entry
    # retrieve the entries from the text boxes
    website_entry_info = website_entry.get()
    email_username_entry_info = email_username_entry.get()
    password_entry_info = password_entry.get()

    # save the entries to a dictionary
    new_data = {
        website_entry_info: {
            "email": email_username_entry_info,
            "password": password_entry_info
        }
    }

    if website_entry_info == "" or email_username_entry_info == "" or password_entry_info == "":
        messagebox.showwarning("Warning", "Please fill in all the details")

    elif website_entry_info != "" and email_username_entry_info != "" and password_entry_info != "":
        is_ok = messagebox.askokcancel(
            "Save", f"These are the details you entered:\n\nWebsite: {website_entry_info}\nEmail/Username: {email_username_entry_info}\nPassword: {password_entry_info}\n\nDo you want to save these details?")
        if is_ok:
            try:
                # get the json data
                with open('password_manager/data.json', 'r') as json_data:
                    data = json.load(json_data)
                # update data
                data.update(new_data)
                # save the json data
                with open('password_manager/data.json', 'w') as json_data:
                    json.dump(data, json_data, indent=4)
                messagebox.showinfo("Save", "Your details have been saved")
            except FileNotFoundError:
                with open('password_manager/data.json', 'w') as json_data:
                    json.dump(new_data, json_data, indent=4)
                messagebox.showinfo("Save", "Your details have been saved")

            # clear the text boxes
            website_entry.delete(0, END)
            password_entry.delete(0, END)


def find_password():
    global website_entry

    # retrieve the entries from the text boxes
    website_entry_info = website_entry.get()

    try:
        # get data.json
        with open('password_manager/data.json', 'r') as json_data:
            data = json.load(json_data)

    except FileNotFoundError:
        messagebox.showwarning("Warning", "No data found")

    else:
        try:
            website = data[website_entry_info]

        except KeyError:
            messagebox.showwarning(
                "Warning", "No details for the website exist.")

        else:
            email = data[website_entry_info]["email"]
            password = data[website_entry_info]["password"]
            messagebox.showinfo(website_entry_info,
                                f"Email/Username: {email}\nPassword: {password}")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("My Pass")
window.config(padx=20, pady=20)

canvas = Canvas(window, width=200, height=200)
logo = PhotoImage(file="password_manager/logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(row=0, column=1)


website_label = Label(window, text="Website:")
website_label.grid(row=1, column=0)


website_entry = Entry(window)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.config(width=35)
website_entry.focus()

search_button = Button(window, text="Search", command=find_password)
search_button.grid(row=1, column=2)
search_button.config(width=20)


email_username_label = Label(window, text="Email/Username:")
email_username_label.grid(row=2, column=0)
email_username_label.config(width=35)
email_username_entry = Entry(window)
email_username_entry.grid(row=2, column=1, columnspan=2)
email_username_entry.config(width=35)
email_username_entry.insert(0, "harunaoseni23@gmail.com")

password_label = Label(window, text="Password:")
password_label.grid(row=3, column=0)

password_entry = Entry(window)
password_entry.grid(row=3, column=1, columnspan=2)
password_entry.config(width=35)

generate_password_button = Button(
    window, text="Generate Password", command=generare_password)
generate_password_button.grid(row=3, column=2)
generate_password_button.config(width=21)


add_password_button = Button(window, text="Add", command=save)
add_password_button.grid(row=4, column=1, columnspan=2)
add_password_button.config(width=30)


window.mainloop()
