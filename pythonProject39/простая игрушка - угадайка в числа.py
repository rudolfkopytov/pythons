import random
game = True
while game:
    num = int(input("Your number:"))
    if num == random.randint(0,10):
        print("You win!")
        break
    else:
        print("You lose!")