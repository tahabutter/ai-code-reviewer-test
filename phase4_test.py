import os

x=1
y=2

def calc():
    a=10
    b=20
    print("Starting calculation")  # debug print
    
    long_variable_name = "This is a very very very very very very very very very very long line to trigger lint error"
    
    if a<b:
        print("a is smaller")

    unused_var = 100

calc()
