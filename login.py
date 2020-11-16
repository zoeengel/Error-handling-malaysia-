# ZOE ENGEL
# CLASS 1

from tkinter import *
from tkinter import messagebox

window = Tk()
window.geometry("300x220")
window.title("Authentification")

# WINDOW HEADER
head_lbl = Label(window, text="Please enter login details\n")
head_lbl.pack(side=TOP)

# USERNAME LABEL AND ENTRY
user_lbl = Label(window, text="Username:")
user_entry = Entry(window, width=25)
user_lbl.pack(side=TOP)
user_entry.pack(side=TOP)

# PASSWORD LABEL AND ENTRY
passwrd_lbl = Label(window, text="\nPassword:")
passwrd_entry = Entry(window, width=25, show="*")
passwrd_lbl.pack(side=TOP)
passwrd_entry.pack(side=TOP)


# LOGIN FUNCTION
def login():
    users = {"user1": "1", "user2": "2", "user3": "3", "user4": "4"}
    usernames = user_entry.get()
    userpass = passwrd_entry.get()
    if (usernames, userpass) in users.items():
        messagebox.showinfo("Login Status", "Succesfull")
        window.withdraw()
        import malaysia
        malaysia.malaysia()
    else:
        messagebox.showinfo("ERROR", "Incorrect username/password")
        user_entry.delete(0, END)
        passwrd_entry.delete(0, END)



# LOGIN BUTTON
HEIGHT = 1
WIDTH = 12
login_btn = Button(window, text="Login", width=WIDTH, height=HEIGHT, command=login)
login_btn.config(bg="lime")
login_btn.pack(side=TOP)

window.mainloop()
