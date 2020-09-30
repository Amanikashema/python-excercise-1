def my_list():
    list = []
    n = int(input("Enter the number of element: "))
    for i in range(1,n):
        new_list = int(input("Enter your desired number:"))
        list.append(new_list)
    a = tuple(list)
    print("My tuple list:", a)
    print("Maximum:", max(a))
    print("Minimum:", min(a))
    print("Sum:", sum(a))

my_list()



