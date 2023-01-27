import random

print("Let's play Heads or Tails \n")
#user picks guess, heads or tails
choice = input.lower("Heads or Tails? \n")
#user flips coin
toss = input("Press the 0 key to toss the coin \n")

#coin flips, randomly lands heads or tails, or drops coin if user entered incorrect key
if toss == "0":
    randchoice = random.randint(1,2)
    if randchoice == 1:
        print("The coin is... Heads")
    else:
        print("The coin is... Tails")
else:
    print("Oops, dropped the coin. Let's try again.")
#print whether or not user was correct 
if (choice == "heads" and randchoice == 1):
    print("You did it!")
elif (choice == "tails" and randchoice == 2):
    print("You did it!")
else:
    print("Dang, maybe next time.")