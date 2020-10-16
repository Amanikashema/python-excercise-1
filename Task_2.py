print("************Student Result**************")
s_name=input("Please enter your name:")
s_surname=input("Please enter your surname:")

def average(total_marks):
    av_mark = float(total_marks / 3)
    return av_mark

def mark():

    total_marks=0
    n=3
    while n>=1:
        n=n-1
        marks=int(input("Please Enter your marks:"))
        total_marks=total_marks+marks

    print("total marks:",total_marks,"%")

    av_mark = average(total_marks)
    print("total average:",av_mark,"%")


    if av_mark >= 50:
        print("Congratulations",s_name,s_surname, "You have Passed the Test")

    else:
        print("test failed")

mark()


from datetime import datetime, timedelta
today =datetime.today()

for d in range (10):
    new_date=today + timedelta(days=1)
    today = new_date
    print(new_date.strftime("%Y %m %d"))
