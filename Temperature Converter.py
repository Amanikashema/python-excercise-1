from tkinter import *

root = Tk()
root.title("Temperature convertor")
root.geometry("800x600")


#celcius to farenheit box display
label_1 = LabelFrame(root, text="Celcius to Fahrenheit", padx="40", pady="40")
label_1.pack(fill="both")
label_1.place(x = 100, y =10)
celcius_to_f = Entry(label_1, textvariable="")
celcius_to_f.pack()



label_2 = LabelFrame(root, text="Fahrenheit to Celcius", padx="40", pady="40")
label_2.pack(fill="both")
label_2.place(x = 350, y =10)
farenheit_to_c = Entry(label_2, textvariable="", command = Active_1())
farenheit_to_c.pack()

act_celcius_btn=Button(text="Active-Celcius to Farenheit")
act_celcius_btn.pack()
act_celcius_btn.place(x =120, y = 150)


act_feranheit_btn=Button(text="Active-Feranheit to Celcius")
act_feranheit_btn.pack(side=RIGHT)
act_feranheit_btn.place(x =380, y = 150)

calculate_btn=Button(text="Calculate Conversion")
calculate_btn.pack(side=LEFT)
calculate_btn.place(x = 50, y= 230)


answer=Entry(text="",background="lime")
answer.pack()
answer.place(x=280,y=230)

clear_button=Button(text="Clear")
clear_button.pack(side=RIGHT)
clear_button.place(x = 500, y = 230)





root.mainloop()
