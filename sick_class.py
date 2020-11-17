from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb

root = Tk()
root.title("Sick class App")
root.geometry("500x500")


class Sick:
    def __init__(self, master):
        self.master = master
        self.sickness_code = Entry(root, text="")
        self.var = IntVar(root)
        self.duration = Entry(root, textvariable=self.var)
        self.practice_number = Entry(root, text="")
        self.var2 = IntVar(root)
        self.consult_fees = Entry(root, textvariable=self.var2)
        self.sick_label = Label(root, text="Sickness Code")
        self.duration_label = Label(root, text="Duration of Treatment")
        self.month_weeks = Label(root, text="weeks/Months")
        self.practice_number_label = Label(root, text="Doctors Practice Number")
        self.consult_fees_label = Label(root, text="Scan/Consultation Fee")

        # positioning
        self.sick_label.place(x=20, y=20)
        self.sickness_code.place(x=140, y=20)
        self.duration_label.place(x=20, y=60)
        self.duration.place(x=180, y=60)
        self.month_weeks.place(x=350, y=60)
        self.practice_number_label.place(x=20, y=100)
        self.practice_number.place(x=220, y=100)
        self.consult_fees_label.place(x=20, y=160)
        self.consult_fees.place(x=200, y=160)

        # buttons for cancer and influenza
        self.var3 = IntVar(root)
        self.cancer_button = Radiobutton(root, text="Cancer", variable=self.var3, value=0)
        self.cancer_button.place(x=20, y=200)
        self.influenza_button = Radiobutton(root, text="Influenza", variable=self.var3, value=1)
        self.influenza_button.place(x=20, y=240)

        # result labels for answers
        self.result = Label(root, text="")
        self.result.place(x=20, y=280)
        self.result1 = Label(root, text="")
        self.result1.place(x=20, y=320)

        # calculate button and clear
        self.clear_button = Button(root, text="clear")
        self.clear_button.place(x=420, y=400)


class Cancer(Sick):
    def __init__(self, master):
        super().__init__(master)

        def calculate_cancer():
            medication = 400
            if self.var3.get() == 0:
                if int(self.var2.get()) > 600:
                    mb.showinfo("Message", "Sorry We cannot treat you")
                elif int(self.var2.get()) < 600:
                    amount_paid = medication + self.var2.get()
                    self.result.config(text="Amount Paid for Treatment R" + str(amount_paid))
        self.calculate_button = Button(root, text="Calculate Cancer", command=calculate_cancer)
        self.calculate_button.place(x=20, y=400)


class Influenza():
    def __init__(self, ma):
        super().__init__(master)

        def calculate_influenza():
            medication = float(350.50)
            if self.var3.get() == 1:
                if self.var2.get() > 600:
                    discount = float(2/100)
                    amount_paid = (medication - (medication * discount)) + self.var2.get()
                    self.result.config(text="Amount Paid for Treatment R" + str(amount_paid))
                    mb.showinfo("Message","2% Discount")
                else:
                    amount_paid = medication + self.var2.get()
                    self.result.config(text="Amount Paid for Treatment R" + str(amount_paid))
        self.calculate_button = Button(root, text="Calculate Influenza", command=calculate_influenza)
        self.calculate_button.place(x=220, y=400)


def classes():
    Sick(root)
    Cancer(Sick)
    Influenza(Sick)


classes()
root.mainloop()
