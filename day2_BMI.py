#program for Body Mass Index
weight = float(input("Enter your weight please"))
height = float(input("Enter your height please"))
BMI = weight/height**2
print("your BMI is {}".format(BMI))
if BMI>25:
    print("you are overweighted try to lose weight!")
elif BMI>=18 and BMI<=25:
    print("you are doing fine.")
else:
    print("You are underweighted!")