#generating a list and a tuple
list = []

for i in range(0 , 4):
    input_list = int(input("Enter input element:"))
    list.append(input_list)
print("user list: ",list)

tuple = tuple(list)
print('Tuple : ',tuple)


