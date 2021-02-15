#user enter a number 
number = int(input("Please enter the number you want to check it is prime \n"))

def is_prime(number):
    dividers = [1,number]
    for i in range(1,number,1):
        if i not in [1,number]:
            if number % i == 0:
                dividers.append(i)


        
    if len(dividers) <2:
        print("This is a prime number")
    else:
        print(f"this number is not prime and can be divided by : {dividers}" )            

is_prime(number)
