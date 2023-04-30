import random
char="abcdefghijklmnopqrstuvwkyzABCDEFGHIJKLMNOPQRSTUVWKYZ1234567890@!#$%&**/+-()[]{}?`~"
while 1:
       password_len=int(input("enter the length of password :"))
       password_count=int(input("no. of password :"))
       for x in range(0,password_count):
           password = ""
           for x in range(0,password_len):
             password_char=random.choice(char)
             password=password + password_char
           print("here is your password",password)
       break
