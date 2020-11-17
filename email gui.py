from tkinter import *
from smtplib import SMTP


root = Tk()
root.title("email")
root.geometry('500x500')

heading=Label(root,text="Python Email Sending App",height=5,bg="green",fg="black",width=500,font="55")
heading.pack()

sender=StringVar()
receiver=StringVar()
password=StringVar()

sender_email_label=Label(root,text="Sender email")
sender_email_label.place(x=0,y=120)

sender_email_entry=Entry(root,textvariable=sender,width=40)
sender_email_entry.place(x=100,y=120)

receiver_email_label=Label(root,text="Receiver email")
receiver_email_label.place(x=0,y=180)

receiver_email_entry=Entry(root,textvariable=receiver,width=40)
receiver_email_entry.place(x=110,y=180)

password.label=Label(root,text="Password")
password.label.place(x=0,y=250)
password.entry=Entry(root,textvariable=password)
password.entry.place(x=100,y=250)
message=StringVar
message_text=Entry(root,textvariable=message)
message_text.place(x=100,y=290,height=100,width=200)


def send_email():
    server = SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email_entry.get(),password.entry.get())
    server.sendmail(sender_email_entry.get(),receiver_email_entry.get(),message_text.get())
    result_label.config(text="The message has been successfully sent")
    server.close()


send_email=Button(root,text="Send Email",command=send_email)
send_email.place(x=0,y=390)

result_label=Label(root)
result_label.pack()

root.mainloop()
