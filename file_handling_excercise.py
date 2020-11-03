from tkinter import *
from tkinter.ttk import *
from tkinter import filedialog


root = Tk()
root.title("My weekend Activities")
root.geometry('510x550')

l1=Label(root,text="My weekend Activities")
l1.pack()
l1.place(x=200,y=10)

#clear functions
def clear():
    text_box.delete('1.0','end')
    text_box.update()

#exit function
def exit():
     root.destroy()

#textbox
text_box=Text(root,height=10,width=40)
text_box.pack()
text_box.place(x=100,y=40)

#global variable filename
global filename
filename = 'My_weekend_activities.txt'

#creat function
def crtbutton():
    global filename
    if filename == 'My_weekend_activities.txt':
        filename=filedialog.asksaveasfile(mode='w')
    if filename != None:
        text=text_box.get('1.0','end')
        filename.write(text)

#buttons
create_but=Button(root,text="Create Textfile",command=crtbutton)
create_but.pack()
create_but.place(x=10,y=260)

#display function
def display():
    global filename
    filename=filedialog.asksaveasfile(mode='r')
    if filename != None:
        text=filename.read()
        text_box.insert('0.0',text)
        text_box.focus()

#display button
display_but=Button(root,text="Display",command=display)
display_but.pack()
display_but.place(x=130,y=260)

#append function
def append():
    with open("My_weekend_activities.txt","a") as text:
        text.write(text_box.get('1.0','end'))

#append button
append_but=Button(root,text="Append",command=append)
append_but.pack()
append_but.place(x=225,y=260)

#clear button
clear_but=Button(root,text="Clear", command=clear)
clear_but.pack()
clear_but.place(x=320,y=260)

#exit button
exit_but=Button(root,text="Exit",command=exit)
exit_but.pack()
exit_but.place(x=420,y=260)


mainloop()
