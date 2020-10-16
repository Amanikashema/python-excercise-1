import random
print("*******Lets Play game , Lets Try To Guess the winning Secret Number*****")

secret_number=random.randint(1,20)
tries=5


while tries!=0:
    user_number=int(input("Please Enter your winning selection number:"))
    tries = tries-1
    if user_number >secret_number:
        print("Your number is too high!!!", "\ntries left:",tries)
    elif user_number < secret_number:
        print("Your number is too low!!!","\ntries left:",tries)
    elif user_number==secret_number:
        print("Congratulations You Have won The Game!!!!")
        break

if tries == 0:
    print("You have lost the game and the winning selection is:",secret_number)
