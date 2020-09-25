print("************Salary employees Check***************")
annual_salary = int(input("Please enter your annual salary:R "))
contract_type = input("what is your contract type: ")

if contract_type == "full-time":
    print("***Full time Employee***")
    income_tax = float(input("Please enter your income tax without percentage sign:"))
    gross_monthly_salary = (annual_salary/12)
    monthly_tax = (income_tax/12)
    net_monthly_salary = (gross_monthly_salary) - (gross_monthly_salary*0.295)
    print("Gross monthly salary:R", gross_monthly_salary)
    print("Monthly tax:",monthly_tax)
    print("Net monthly salary:R",net_monthly_salary)


elif contract_type == part-time:
    print("***Part Time***")
    income_tax = float(input("Please enter your income tax without percentage sign:"))
    gross_monthly_salary = (annual_salary/12)
    monthly_tax = (income_tax/12)
    net_monthly_salary = (gross_monthly_salary) - (gross_monthly_salary*0.25)
    print("Gross monthly salary:R", gross_monthly_salary)
    print("Monthly tax:",monthly_tax)
    print("Net monthly salary:R",net_monthly_salary)










