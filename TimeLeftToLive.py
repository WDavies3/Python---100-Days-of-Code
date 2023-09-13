#Calculate how many days, weeks, and months the user has left to live
#assuming the user lives til 90.  We are calculating each independent of
#the other meaning they are not combined

#Get the user's age
age = int(input("How old are you? "))
years_to_live = 90 - age
if age > 90:
    print("You've lived long enough.  You need to stop wasting oxygen!!!")
else:
    months = years_to_live * 12
    weeks = years_to_live * 52
    days = years_to_live * 365
    print(f"You have {years_to_live} years left to live.  That is {months} in months, {weeks} in weeks, and {days} in days.")
