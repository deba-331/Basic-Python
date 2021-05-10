import random

max_value=6
min_value=1

roll_dice="yes"

while roll_dice=='yes' or roll_dice=='y':
    print("rolling the dice")
    print("the values are")
    
    print(random.randint(min_value,max_value))
    print(random.randint(min_value,max_value))
    
    roll_dice=input("Want to roll again?")

