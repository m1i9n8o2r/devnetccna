def devnet():
    ' ' ' prints simple function' ' '
    print("prints simple function")

def sub(arg1, arg2):
    '''returns the sub of 2 arguments'''
    result = arg1 - arg2
    print (result)

def hello(*args):
    for arg in args:
        print("Hello", arg, "!")

def hello2(**kwargs):
    for key, value in kwargs.items():
        print("Hello", value, "!")


devnet()
help(devnet)

sub(10, 5)
help(sub)

hello("Carlos", "Maria")

hello2(kwarg1="Minor", kwarg2="Jessica")

