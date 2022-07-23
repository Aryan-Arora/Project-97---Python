import random
from winreg import REG_NO_LAZY_FLUSH 

a=random.randint(1,9)

chances=0

while chances<5:
    b=int(input("Enter Your Guess"))
    if a==b:
        print("Congratulations You Won")
    elif a<b:
        print("Your Guess is Too Large")
    else:
        print("Your Guess is Too small")

    chances+=1

if chances>5 :
    print("You Lose The number Was ", a)