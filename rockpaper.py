#this is a game of rock paper scissors using a random number generator
#by Ashley Cook
def main():
    import random
    from time import sleep
    #rock paper and scissors text art functions
    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''

    print("This is a game of Rock, Paper, Scissors.\n")
    sleep(1)
    #ask for user input
    options = ["Rock", "Paper", "Scissors"]
    userchoice = input("Type 0 to play Rock, type 1 to play Paper, or type 2 to play Scissors.\n")
  

    #computer input
    compchoice = random.choice(options)
    #countdown
    from time import sleep
    sleep(2)   
    print("3")
    sleep(1)
    print("2")
    sleep(1)
    print("1")
    #display user choice
    print("You played... \n")
    if userchoice == "0":
        userchoice = options[0]
        print(options[0])
        print(rock)
    elif userchoice == "1":
        userchoice = options[1]
        print(options[1])
        print(paper)
    else:
        userchoice = options[2]
        print(options[2])
        print(scissors)
    #display comp choice
    print("The computer played... \n")
    print(compchoice)
    if compchoice == options[0]:
        print(rock)
    elif compchoice == options[1]:
        print(paper)
    else:
        print(scissors)
    #result
    sleep(1)
    if userchoice == options[0] and compchoice == options[2]:
        print("You won!")
    elif userchoice == options[1] and compchoice == options[0]:
        print("You won!")
    elif userchoice == options[2] and compchoice == options[1]:
        print("You won!")
    elif userchoice == options[0] and compchoice == options [1]:
        print("You lost!")
    elif userchoice == options[1] and compchoice == options[2]:
        print("You lost!")
    elif userchoice == options[2] and compchoice == options[0]:
        print("You lost!")
    else:
        print("You tied!")
    #say goodbye
    sleep(2)
    print("Thanks for playing!")

   

