year=int(input("enter a year please"))
if year % 4 ==0 and year % 100 !=0:
    print("this year is leap")
elif year % 400 == 0 :
    print("this is a leap year")
else:
    print(year," is not a leap year")