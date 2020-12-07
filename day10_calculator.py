# calculator project
from day10 import logo

def addition(a,b):
    return a + b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a/b
def substraction(a,b):
    return a - b

should_continue = True

operations = {"+":addition,"*": multiplication,"/":division,"-":substraction }
for symbol in operations:
    print(symbol)

while should_continue:
    print(logo)
    choice = input("pick an operation ")
    if choice not in operations:
        continue
    operation = operations[choice]
    a=float(input("enter the first number"))
    b=float(input("enter the seconde number"))
    answer = operation(a,b) 
    print("the result is ",answer)
    should_continue = input("Do you want to do another operation type 'yes' or 'no'\n")
    if should_continue == "no":
        should_continue = False
    if input("To continue with  the result of the previous operation as first number type yes else type no") == "yes":
        a = answer
        choice = input("pick an operation ")
        operation = operations[choice]
        b=float(input("enter the seconde number"))
        answer = operation(a,b) 
        print("the result is ",answer)
        


