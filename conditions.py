# Classify a persons age group: child(<13),Teenager(13-19), adult(20-59) and senior(60+).

# age=int(input("Enter your age"))
# if age<13:
#     print("you are a child.")
# elif age>=13 or age<=19:
#     print("you are an adult.")
# elif age>19 or age<60:
#     print("you are an adult.") 
# else:
#     print("you are a senior.")

#MOVIE Tickets are priced based on age:$12 for adults,$8 for children.Everyone gets a $2 
#discount on wednesday.

# age=int(input("Enter your age:"))
# day=input("Enter your day:")
# if age>=18:
#     price=12
# else:
#     price=8
# if day=="wednesday":
#         price=price-2
# print("You have to pay$",price)

# Assign a Letter grade based on a student's score: A(90-100),B(80-89),C(70-79),D(60-69),F(Below60)

# score=int(input("Enter your score:"))
# if score>=101:
#     print("Check your grade again...")
#     exit()
# if score>=90:
#     print("You have got A grade.")
# elif score>=80 or score<90:
#     print("You have got B grade.")
# elif score>=70 or score<80:
#     print("You have got C grade.")
# elif score>=60 or score<70:
#     print("You have got D grade.")
# else:
#     print("You have got F grade.")

#Determine if a fruit is ripe,overripe or unripe based on its color(eg. Banana:- Green-unripe,
# yellow-ripe, Brown-overripe.

# fruit="banana"
# color="yellow"
# if fruit=="banana":
#     if color=="green":
#         print("the banana is unripe.")
#     elif color=="yellow":
#         print("the banana is ripe.")
#     elif color=="brown":
#         print("the banana is overripe.")
#     else:
#         print("Cant determine.")
# else:
#     print("Cant determine.")

#customize a coffee order:"small","medium",or "large" with an option for "Extra shot of expresso".

# order_size="medium"
# extra_shot=True
# if extra_shot:
#     coffee=order_size + " coffee with extra shot of expresso."
# else:
#     coffee=order_size + "coffee"
# print("order:",coffee)

#Determine if a year is a Leap year.(Leap years are divisible by 4,but not 100 unless also  divisible by 400).

# year=int(input("Enter a year:"))
# if (year%400==0) or (year%4==0 and year%100!=0):
#     print(year," is a leap year.")
# else:
#     print(year," is NOT a leap year.")


