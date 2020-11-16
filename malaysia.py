# ZOE ENGEL
# CLASS 1

from tkinter import *
from tkinter import messagebox
window = Tk()
window.geometry("320x120")
window.title("Vacation")

amountlbl = Label(window, text="Please enter amount in your account:\n")
amountlbl.pack(side=TOP)
amounten = Entry(window)
amounten.pack(side=TOP)

def malaysia():

    amount = int(amounten.get())
    try:
         if amount < 3000:
             raise ValueError(messagebox.showinfo("Message","Please deposit more funds for this excursion!"))
    except ValueError as e:
        print(e)
        amounten.delete(0, END)
    # except TypeError:
    #     print("incorrect entry")
    else:
              messagebox.showinfo('Message',"You qualify for a trip to Malaysia!")
              amounten.delete(0, END)
    finally:
        print("Transaction complete!")


def exit():
    window.destroy()


# EXIT BUTTON
extbtn = Button(window, text="Exit", command=exit)
extbtn.config(bg="lime")
extbtn.pack(side=BOTTOM)

# QUALIFICATION BUTTON
checkbutton = Button(window, text="Check qualification", command=malaysia)
checkbutton.config(bg="lime")
checkbutton.pack(side=TOP)
window.mainloop()
