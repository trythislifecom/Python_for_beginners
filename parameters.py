# functions with parameters

def add(x,y):
    return x+y


a = int(input("Enter first value: "))
b = int(input("Enter second value: "))
print(f"The sum of {a} and {b} is = {(add(a,b))}")


# converters by using functions

def temp(c):
    f = (9/5)*c+32
    return f

c = int(input("Enter temperature in cel: "))
print(f"the temperature is {temp(c)}")