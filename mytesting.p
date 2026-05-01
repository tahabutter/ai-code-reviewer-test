import os

a = 5
b = 10

def myFunc():
    x=1
    y=2
    print("Debugging start")   # should trigger warning
    
    long_variable_name = "This is a very very very very very very very very very very long line that should trigger lint"
    
    if a<b:
        print("a is less than b")

myFunc()
