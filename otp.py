# otp that valid for only one login session
def otp():
    import random
    re=random.random()
    return str(re)[-4:] #slicing of -4 for four digit otp
# main code
out=otp()
print(out)


