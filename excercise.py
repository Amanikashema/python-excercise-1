#displaying names and email
first_name = input("Please enter your first name:")
second_name = input("Please enter your second name:")
age = input("how old are you:")
full_name = first_name + " " + second_name
email_address = first_name + second_name + "@gmail.com"
print("Hello " + full_name + " You are " + age + " Old and you email address is " + email_address)


#calculation of net pay for emploiyees

income_tax = 0.15
salary = int(input("Please  enter your salary: "))
net_pay = salary - (salary*income_tax)
print("Your total net pay =" , net_pay)
