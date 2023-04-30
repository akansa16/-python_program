import random
# in guess no. program the no. is guess by the player that computer choose
att=int(input("enter no. of attempt:")) # no. of attempt to increase accuracy of progam
n=int(input("range of no.:"))
a=random.randint(1,n)#COMPUTER ENTER THE NUMBER
while att:
    n=int(input("No. enter by player:"))
    if n<a:
        print("no. is small",n)
    elif n>a:
        print("no. is larger",n)
    else:
        print("you guess correct no.",n)
        print("congratulation")
        break
    att=att-1
    print("no. of attempt remain",att)
else:
    print("you loose the game")

