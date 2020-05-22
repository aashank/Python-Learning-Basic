from random import randint
answer = randint(1,10)
while True:
    try:
        print(answer)  # this is the cheating and a one way to know the answer before entering it in the game.
        guess=int(input("Enter number 1 to 10 : "))
        if 0 < guess < 11:
            if guess==answer:
               print("You are genious")
               break
        else:
            print("Hey bimbo, I said please enter number from 1 to 10")
    except ValueError:
        print("Please Enter a Number")