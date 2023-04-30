import random
def hangman():
    ls=['raunak','akanksha','shwechha','mandvi','anuradhika']
    com=random.choice(ls)
    att=10
    guessmade=''
    valid_entry=set('abcdefghijklmnopqrstuvwxyz')
    while len(com)>0:
       main_word=""

       for letter in com:
         if letter in guessmade:
            main_word=main_word+letter
         else:
            main_word=main_word+"_"

       if main_word==com:
         print(main_word)
         print("you won !!!")
         break

       print("guess the words",main_word)
       guess=input()

       if guess in valid_entry:
         guessmade=guessmade + guess
       else:
         print("enter valid character")
         guess=input()

       if guess not in com:
         att=att-1
         if att==9:
           print("9 attempt left!!!")
           print("---------------")
         if att==8:
           print("8 attempt left!!!")
           print("---------------")
           print("       o       ")
         if att==7:
           print("7 attempt left!!!")
           print("---------------")
           print("       o       ")
           print("       |       ")
         if att == 6:
           print("6 attempt left!!!")
           print("---------------")
           print("       o       ")
           print("       |       ")
           print("      /        ")
         if att == 5:
           print("5 attempt left!!!")
           print("---------------")
           print("       o       ")
           print("       |       ")
           print("      / \      ")
         if att == 4:
           print("4attempt left!!!")
           print("---------------")
           print("      \o       ")
           print("       |       ")
           print("      / \      ")
         if att == 3:
           print("3 attempt left!!!")
           print("---------------")
           print("      \o/       ")
           print("       |      ")
           print("      / \      ")
         if att == 2:
           print("2 attempt left!!!")
           print("---------------")
           print("      \o/ |     ")
           print("       |       ")
           print("      / \       ")
         if att == 1:
           print("only 1 attempt left!!!")
           print("---------------")
           print("      \o/_|       ")
           print("       |       ")
           print("      / \       ")
         if att == 0:
           print("you loose the game")
           print("you let a good man die")
           print("---------------")
           print("       o_|       ")
           print("      /|\       ")
           print("      / \       ")
           break


name=input("enter your name ")
print("WELCOME-",name)
print("guess the word in 10 attempt otherwise we hang the man")
hangman()