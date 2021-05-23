import random

print("This is a rock, paper, scissors game.\n")
userInput=input("Enter rock, paper, or scissors.\n")

if userInput=="rock" or userInput =="paper" or userInput == "scissors" :
    computerPlay=random.randint(0,2)
    #key: 0=rock, 1=paper, 2=scissors
    if userInput=="rock" :
        if computerPlay==0 :
            print("You chose rock & the computer chose rock; TIE!!")
        if computerPlay ==1 :
            print("You chose rock & the computer chose paper; YOU LOSE!!")
        if computerPlay ==2 :
            print("You chose rock & the computer chose scissors: YOU WIN!!")
    if userInput=="paper" :
        if computerPlay==0 :
            print("You chose paper and the computer chose rock; YOU WIN!!")
        if computerPlay==1 :
            print("You chose paper and the computer chose paper; TIE!!")
        if computerPlay==2 :
            print("You chose paper and the computer chose scissors; YOU LOSE!!")
    if userInput=="scissors" :
        if computerPlay==0 :
            print("You chose scissors and the computer chose rock; YOU LOSE!!")
        if computerPlay==1 :
            print("You chose scissors and the computer chose paper; YOU WIN!!")
        if computerPlay==2 :
            print("You chose scissors and the computer chose scissors; TIE!!")
else :
    print("ERROR!!")