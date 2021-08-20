import random

min_value = 1
max_value = 6

roll_dice = input("Do you wanna roll dice? ")

while roll_dice in ["yes","YES","Yes","Y","y"]:
    print("Rolling the dice")
    print("The values are: ")
    print("First Number is: ",random.randint(min_value,max_value))
    print("Second Number is: ",random.randint(min_value,max_value))

    roll_dice = input("Roll the dice again? ")

else:
    print("Thanyou, Visit again")