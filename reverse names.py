def rev_name():
    name = input("Please Enter your name: ")
    surname = input("Please Enter your surname: ")
    print("Your name is: ", name[::-1])
    print("Your surname is: ", surname[::-1])
    return name, surname


rev_name()
