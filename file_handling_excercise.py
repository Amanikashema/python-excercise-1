from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfile


root = Tk()
root.title("My weekend Activities")
root.geometry('510x550')

l1=Label(root,text="My weekend Activities")
l1.pack()
l1.place(x=200,y=10)

#functions
def clear():
    text_box.delete(0,END)
    text_box.update()

def exit():
     root.destroy()

#textbox
text_box=Text(root,height=10,width=40)
text_box.pack()
text_box.place(x=100,y=40)

#buttons
create_but=Button(root,text="Create Textfile")
create_but.pack()
create_but.place(x=10,y=260)

display_but=Button(root,text="Display")
display_but.pack()
display_but.place(x=130,y=260)

append_but=Button(root,text="Append")
append_but.pack()
append_but.place(x=225,y=260)

clear_but=Button(root,text="Clear", command=clear)
clear_but.pack()
clear_but.place(x=320,y=260)

exit_but=Button(root,text="Exit",command=exit)
exit_but.pack()
exit_but.place(x=420,y=260)









mainloop()
