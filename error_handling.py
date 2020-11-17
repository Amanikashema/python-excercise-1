from tkinter import*
from tkinter import messagebox
root=Tk()
root.title("Authentification")
root.geometry("400x400")


def login():
    user1 = {"john": "123", "amani": "1234"}
    if user_name_entry.get() in user1.keys() and pass_word_entry.get() in user1.values():
        root = Tk()
        root.title("Exception handling")
        root.geometry("400x400")
        label_2 = Label(root, text="Please Enter amount in your account")
        label_2.place(x=100, y=0)
        amount = Entry(root)
        amount.place(x=140, y=40)
        def decision():
            try:
                if int(amount.get()) >= 3000:
                    messagebox.showinfo("Congratulations","You Qualify for the trip to malaysia")
            finally:
                if int(amount.get()) <= 3000:
                    raise ValueError(messagebox.showinfo("Sorry","Please Deposit more funds in this excursion"))

        check_button = Button(root,text="Check Qualification", command=decision, bg="green")
        check_button.place(x=140, y=80)
    else:
        messagebox.showerror("error","Wrong password or username")


# labels
label_1 = Label(root,text="Please enter your Login details")
user_name_label = Label(root,text="Username")
pass_word_label = Label(root,text="Password")
login_button = Button(root,text="Login",command=login, bg="green")

# Entries
user_name_entry = Entry(root,text="")
pass_word_entry = Entry(root,text="")

# positioning
label_1.place(x=110,y=0)
user_name_label.place(x=80, y=40)
pass_word_label.place(x=80,y=80)
user_name_entry.place(x=160,y=40)
pass_word_entry.place(x=160,y=80)
login_button.place(x=200,y=120)


root.mainloop()

