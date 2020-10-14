from tkinter import *

root = Tk()
root.title("Temperature convertor")
root.geometry("695x350")


#celcius to farenheit box display
label_1 = LabelFrame(root,bg="yellow", text="Celcius to Fahrenheit", padx="40", pady="40")
label_1.pack(fill="both")
label_1.place(x = 100, y =10)


def activate_l1():
    celcius_to_f.configure(state="normal")

celcius_to_f = Entry(label_1, textvariable="",state="disable")
celcius_to_f.pack()

#function for C-F Calculation conversion
def convert():
    if celcius_to_f:
        celcius = float(celcius_to_f.get())
        farenheit = (celcius*9/5+32)
        answer.insert(0,farenheit)

#function for F-C Calculation conversion
def convert1():
    if farenheit_to_c:
        farenheit = float(farenheit_to_c.get())
        celcius = (farenheit-32)*5/9
        answer.insert(0, celcius)



#Farenheit to celcius box display
label_2 = LabelFrame(root,bg="blue",text="Fahrenheit to Celcius", padx="40", pady="40")
label_2.pack(fill="both")
label_2.place(x = 350, y =10)
farenheit_to_c = Entry(label_2, textvariable="", state="disable")
farenheit_to_c.pack()

#button1
act_celcius_btn=Button(text="Activate-Celcius to Farenheit",bg="yellow", command=activate_l1)
act_celcius_btn.pack()
act_celcius_btn.place(x =100, y = 150)


def activate_l2():
    farenheit_to_c.configure(state="normal")

#button2
act_feranheit_btn=Button(text="Activate-Feranheit to Celcius",bg="blue",command=activate_l2)
act_feranheit_btn.pack(side=RIGHT)
act_feranheit_btn.place(x =380, y = 150)

#C-F Button
calculate_btn=Button(bg="yellow", text="C-F",command=convert)
calculate_btn.pack(side=LEFT)
calculate_btn.place(x = 95, y= 230)

#F-C BUutton
calculate_btn=Button(text="F-C",command=convert1, bg="blue")
calculate_btn.pack(side=RIGHT)
calculate_btn.place(x = 560, y= 230)

#Result Box
answer=Entry(text="",background="lime")
answer.pack()
answer.place(x=275,y=230)

#function to clear answer box
def clear():
    celcius_to_f.delete(0,END)
    farenheit_to_c.delete(0,END)
    answer.delete(0,END)

#clear button
clear_button=Button(text="Clear",bg="white", command=clear)
clear_button.pack(side=RIGHT)
clear_button.place(x = 560, y = 290)

#function to quit program
def quit():
    root.destroy()

exit=Button(root,text="Exit Program",bg="red",command=quit)
exit.pack()
exit.place(x=300,y=290)



root.mainloop()
