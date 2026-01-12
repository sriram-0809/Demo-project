from operations import add,  subtract, multiply, divide

print("simple calculator")

a=int(input("enter value a:"))
b=int(input("enter value b:"))

print("Addition of a,b:",add(a,b))
print("Subtraction of a,b:",subtract(a,b))
print("Multiplication of a,b:",multiply(a,b))
print("Division of a,b:",divide(a,b))