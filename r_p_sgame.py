import random
ls=['rock','scissor','paper']
computer=random.choice(ls)#CHOICE OF COMPUTER
player=input("player choice :")
if computer==player:
    print("tie the game")
elif(computer=='rock'and player=='paper'):
    print("player win the game")
elif(computer=='paper' and player=='scissor'):
    print("you win the game")
else:
    print("you loose the game")
