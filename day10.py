#functions with outputs
# firstName = input("Enter your first name please \n")
# lastName = input("Enter your last name please \n")
# def formatted_name(firstName,lastName):
#     formatted_firstName = firstName.title()
#     formatted_lastName = lastName.title()
#     return print("Hello, Mr. {} {}!".format(firstName,lastName))
# formatted_name(firstName,lastName) 

# #days in month
# def leap_year(year):
#     if year % 4 ==0 and year % 100 !=0:
#         return True
#     elif year % 400 == 0 :
#         return True
#     else:
#         return False

# def days_in_month(year,month):
    
#     month_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31] 
#     if leap_year(year) == True:
#         month_days[1] = 29
#         return month_days[month-1]
#     else:
#         return month_days[month-1]
  
  
# #🚨 Do NOT change any of the code below 
# year = int(input("Enter a year: "))
# month = int(input("Enter a month: "))
# days = days_in_month(year, month)
# print(days)

# calculator project

# def addition(a,b):
#     return a + b
# def multiplication(a,b):
#     return a * b
# def division(a,b):
#     return a/b
# def substraction(a,b):
#     return a - b

# should_continue = True
# while should_continue:
#     choice = int(input("which operation do you want to do ? (type the number of operation) :\n1.multiplication\n2.division\n3.addition\n4.substraction\n"))
#     a=float(input("enter the first number"))
#     b=float(input("enter the seconde number"))
#     if choice == 1:
#         print(multiplication(a,b))
#     elif choice == 2 :
#         print(division(a,b))
#     elif choice == 3:
#         print(addition(a,b))
#     elif choice == 4:
#         print(substraction(a,b))
#     else: 
#         print("wrong choice please try again")
#     should_continue = input("Do you want to do another operation type 'yes' or 'no'\n")
#     if should_continue == "no":
#         should_continue = False
logo = """
 _____________________
|  _________________  |
| | Pythonista   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
