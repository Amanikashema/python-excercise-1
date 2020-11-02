from tkinter import *
from tkinter import ttk
root = Tk()
root.title("Ticket sales")
root.geometry("600x600")

class Easyticket:
    def __init__(self,master):
        self.master = master
        self.soccer = 40
        self.movie = 75
        self.theater = 100

        #function for clearing selection
        def clear():
            self.cell_entry.delete(0,END)
            self.ticketbought.delete(0,END)

#layout
        #cell number entry
        self.label_1 = Label(root,text="Enter CellNumber:")
        self.label_1.pack()
        self.label_1.place(x=50,y=50)
        self.var = IntVar(root)
        self.var.set(0)
        self.cell_entry=Entry(root,textvariable=self.var)
        self.cell_entry.pack()
        self.cell_entry.place(x=300,y=50)

        #category selection
        self.label_2 = Label(root,text="Select Ticket Category:")
        self.label_2.pack()
        self.label_2.place(x=50,y=150)
        self.var=StringVar(root)
        self.var.set("Select Ticket")
        self.dropmenu=OptionMenu(root,self.var,"soccer","movie","theater")
        self.dropmenu.pack()
        self.dropmenu.place(x=300,y=140)

        #Number of ticket bought selection option
        self.label_3= Label(root,text="Number of Tickets Bought")
        self.label_3.pack()
        self.label_3.place(x=50,y=250)
        self.var2 = IntVar(root)
        self.var2.set(0)
        self.ticketbought = Spinbox(master,textvariable=self.var2, from_=0, to=100)
        self.ticketbought.pack()
        self.ticketbought.place(x=300,y=250)

         #cear button
        self.clear_button = Button(root,text="Clear",bg="grey", command=clear)
        self.clear_button.pack()
        self.clear_button.place(x=400,y=350)

        #condionals for selections in option menu
        def calcpayment():
            vat=0.14
            if self.var.get()=="soccer":
                price=40
                amountpayable=int(self.ticketbought.get())*price+vat
                self.result.config(text="Amount Payable:"+ str(amountpayable) + "\n" + "Reservation for Soccer for "+str(self.ticketbought.get()) + "\n" +"Was done by "+ str(self.cell_entry.get()))
            if self.var.get()=="movie":
                price=75
                amountpayable=int(self.ticketbought.get())*price+vat
                self.result.config(text="Amount Payable:"+ str(amountpayable) + "\n" + "Reservation for Movies for "+str(self.ticketbought.get()) + "\n" +"Was done by "+ str(self.cell_entry.get()))
            if self.var.get()=="theater":
                price=100
                amountpayable=int(self.ticketbought.get())*price+vat
                self.result.config(text="Amount Payable:"+ str(amountpayable) + "\n" + "Reservation for Theater for "+str(self.ticketbought.get()) + "\n" +"Was done by "+ str(self.cell_entry.get()))

        #result label
        self.result=Label(root,text="",width=30,bg="green")
        self.result.pack()
        self.result.place(x=190,y=450)


        #calculate button
        self.calculate_button= Button(root,text="Calculate Ticket",bg="blue",command=calcpayment)
        self.calculate_button.pack()
        self.calculate_button.place(x=50,y=350)



my_gui=Easyticket(root)

root.mainloop()

