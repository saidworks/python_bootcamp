
#get the work week using datetime module
import datetime
my_date = datetime.date.today() 
year, week_num, day_of_week = my_date.isocalendar()
print("Week #" + str(week_num) + " of year " + str(year))