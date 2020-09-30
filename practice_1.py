print("********************A list of ages of different people*************")
#function to find the maximum value in the list
#def list():
#    ages = [2,12,12,14,15,16,17,18,14,20,20]
#    return max(ages)

#print("The maximum number is: ", list())

#function to remove duplicate numbers
#def convert(ages):
#   return set(ages)
#ages=[2,12,12,14,15,16,17,18,14,20,20]
#print("New list with no duplication: ", convert(ages))


#comparison of two list

ages=[2,12,12,14,15,16,16, 17,18, 14, 20, 20]
ages1=[2,4,12,14,15,16,16, 17,18, 14, 20, 20]

def common(ages,ages1):

    if len(ages) != len(ages1):
        return false
    for i in ages:
        if i not in ages1:
            return False
    return True

if common(ages,ages1):
    print("have common number:")
    a = set(ages) & set(ages1)
    print(a)

else:
    print("None common")



