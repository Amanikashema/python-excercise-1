print("************************Bright Light Company*********************************")
dept_code = input("Please enter your department code: ")
current_annual_salary = int(input("Please enter your annual salary: "))
if dept_code == "A" or "a":
    a = float(0.072)
    current_monthly_salary = (current_annual_salary/12)
    increased_salary = current_monthly_salary + (current_monthly_salary*a)
    print("Normal monthly salary:R",current_monthly_salary)
    print("Increased monthly salary:R",increased_salary)
    print("********************CONGRATULATIONS ON YOUR RAISE***************************")

elif dept_code == "B" or "b":
    a = float(0.068)
    current_monthly_salary = (current_annual_salary/12)
    increased_salary = current_monthly_salary + (current_monthly_salary*a)
    print("Normal monthly salary:R",current_monthly_salary)
    print("Increased monthly salary:R",increased_salary)
    print("********************CONGRATULATIONS ON YOUR RAISE***************************")

else:
    a = float(0.063)
    current_monthly_salary = (current_annual_salary/12)
    increased_salary = current_monthly_salary + (current_monthly_salary*a)
    print("Normal monthly salary:R",current_monthly_salary)
    print("Increased monthly salary:R",increased_salary)
    print("********************CONGRATULATIONS ON YOUR RAISE***************************")







