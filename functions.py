# write a funtion to calculate and return the square of a number.

# num=int(input("Enter a number: "))
# def square_of_number(num):
#     return num**2
# result=square_of_number(num)
# print(result)

#Create a function that takes two numbers as a parameter and returns their sum.

# def sum_of_numbers(a,b):
#     return a+b
# sum=sum_of_numbers(10,12)
# print(sum)

#Create a function multiply() that multiplies two numbers but can also accept and multiply strings.

# def multiply(a,b):
#     return a*b
# result1= multiply(2,3)
# result2= multiply("a",3)
# result3= multiply(2,"b")
# print(result1)
# print(result2)
# print(result3)

#Create a function that returns both the area and circumference of a circle given its radius.

# import math
# def circle(radius):
#     area=math.pi*radius*radius
#     circumference=2*math.pi*radius
#     return round(area,0),round(circumference,0)   #round method to make decimal point upto 2   
# a,b=circle(7)
# print("area:",a)
# print("circumference:",b)

#write a function that greets a user. If no name is provided,it should greet with default name.

# def greet(name=" user"):
#     return "Hello" + name +"!"
# print(greet())                     #name is not provided. so default which is user will be output.
# print(greet(" Bishal"))            #name is provided

#Create a Lambda function to compute the cube of a number.

# cube=lambda x: x**3
# print(cube(3)) 

#Write a function that takes variable number of agruments and returns their sum.

# def sum_of_all(*args):
#     print(args)
#     return sum(args) 
# print(sum_of_all(1,2,3))
# print(sum_of_all(1,2,3,4,5,6,7,8,9,10))

#Create a function that accepts any number of keyword arguments and prints them in the 
#format:  (  key:value   )

# def print_kwargs(**kwargs):
#     for key,value in kwargs.items():
#         print(f"{key}:{value}")
# print_kwargs( Name="Bishal", Power="Learn")
# print_kwargs( Name="Kashish B")
# print_kwargs( Name="Bishal", Power="Learn", anime="Naruse")
 
#Write a generator function that yields even numbers upto a specified limit.

# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i

# for num in even_generator(10):
#     print(num)

#Create a recursive function to calculate the factorial of a number.

# def factorial_of_num(num):
#     if num==0:
#         return 1
#     elif num==1:
#         return 1
#     else:
#         return num*factorial_of_num(num-1)
# print(factorial_of_num(1))


