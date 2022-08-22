from tkinter import *
BACKROUND = "#fffde3"
FONT_NAME = "Courier"
ACTIVE_FILL_BUTTON = "#E64848"
from tkinter import messagebox
from random import randint, shuffle, choice
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def password_generator():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8,10))]
    password_symbols = [choice(symbols) for _ in range(randint(2,4))]
    password_numbers = [choice(numbers) for _ in range(randint(2,4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)

    input_pass.delete(0, 'end')
    input_pass.insert(0, password)
    pyperclip.copy(password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_clicked():
    email = input_email.get()
    website = input_website.get()
    password = input_pass.get()

    if len(email) == 0 or len(website) == 0 or len(password) == 0:
        messagebox.showerror(title="Oops", message="Please don't leave any fields empty")
    else:
        is_ok = messagebox.askokcancel(title=website,
                                       message=f"These are the details entered: \nEmail: {email}\nPassword: {password}"
                                               f"\nIs it ok to save?")
        if is_ok == True:
            with open("data.txt", mode ="a") as data_file:
                data_file.write(f"{website} | {email} | {password} \n")
            input_website.delete(0, 'end')
            input_pass.delete(0, 'end')

# ---------------------------- UI SETUP ------------------------------- #
# TODO: 1. Open the Window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKROUND, )

#TODO: 2. Canvas (create image)
canvas = Canvas(width=200, height=200, bg=BACKROUND, highlightthickness=0)
logo = PhotoImage(file='logo.png')
canvas.create_image(100,100, image=logo)
canvas.grid(column=1, row=0)

#TODO: 3. Create a label of Website and input
website_label = Label()
#print(website_label.config().keys())
website_label.config(text="Website:", bg=BACKROUND)
website_label.grid(column=0, row=1)

#TODO: 3.1 Create and iput box
input_website = Entry(width=46)
input_website.grid(column=1, row=1, columnspan=2)
input_website.focus()



#TODO: 4. Create a lablel of Email/Username:
email_label = Label()
email_label.config(text="Email/Username:", bg=BACKROUND)
email_label.grid(column=0, row=2)


#TODO: 4.1 Create and iput box
input_email = Entry(width=46)
input_email.grid(column=1, row=2,  columnspan=2)
input_email.insert(0,"Leonid.yatskevich@gmail.com" )


#TODO: 5. Create a label of Password:
pass_label = Label()
pass_label.config(text="Password:", bg=BACKROUND)
pass_label.grid(column=0, row=3)

#TODO: 5.1 Create and iput box
input_pass = Entry(width=36)
input_pass.grid(column=1, row=3)


#TODO: 5.2 Create button of "generate password"
pass_button = Button()
pass_button.config(text="Generate", bg=BACKROUND, width=7, command=password_generator)
pass_button.grid(column=2, row=3)

#TODO: 6. Create a button "ADD"
add_button = Button()
add_button.config(text="Add", bg=BACKROUND, width=39, command=add_clicked)
add_button.grid(column=1, row=4,  columnspan=2)






window.mainloop()