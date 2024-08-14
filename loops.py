#Given a list of numbers, count how many are positive.
# numbers=[1,-2,3,-4,5,6,-7,-8,9,10]

# numbers=[1,-2,3,-4,5,6,-7,-8,9,10]
# count_positive_numbers=0
# for i in numbers:
#     if i>0:
#         count_positive_numbers+=1
# print("Number of postive numbers :",count_positive_numbers)

#calculate the sum of even numbers up to a given number n.

# num=int(input("Enter a number."))
# sum_even=0
# for i in range(1,num+1):
#     if i%2==0:
#         sum_even+=i
# print("Sum of even numbers is :",sum_even)

#print the multiplication table of a given number upto 10, but skip the fifth iteration.

# num=int(input("Enter any number you want ."))
# for i in range(1,11):
#     if i==5:
#         continue
#     print(num,"X",i,"=",num*i)

#Reverse a string using a loop.

# input_string="python"
# reverse_string=""
# for i in input_string:
#     reverse_string=i + reverse_string
# print(reverse_string)

#Given a string, find the first non-repeated character.

# input_str="teeter"
# for char in input_str:
#     print(char)
#     if input_str.count(char)==1:
#         print("char is:",char)
#         break

#compute the factorial of a number using while loop.

# num=int(input("Enter a number:"))
# factorial=1
# while num>0:
#     factorial=factorial*num
#     num=num-1
# print("Factorial:",factorial) 

#keep asking the use for input until they enter a number 1 and 10.

# while True:
#     num=int(input("Enter a number between 1 and 10."))
#     if 1<=num and num<=10:
#         print("Thanks...")
#         break
#     else:
#         print("Invalid input, Try again")

#Check if a number is a prime number.

# num=int(input("Enter a number."))
# is_prime=True

# while num>1:
#     for i in range(2,num):
#         if num%i==0:
#             is_prime=False
#             break
# print(is_prime)

#check if all the elements in the list are unique. If a dupllicate is found then exit the loop and return the duplicates.    item=["apple","banana","orange","apple",",mango"]

# items=["apple","banana","orange","apple","mango"]
# unique_item=set()
# for item in items:
#     if item in unique_item:
#         print("Duplicate:",item)
#         break
#     unique_item.add(item)

#Implement an eponential backoff strategy that doubles the wait time between retries, starting from 1 seconds, but stops after 5 retries.

# import time
# wait_time=1
# max_retries=5
# attemps=0

# while(attemps<max_retries):
#     print("Attmpts:",attemps+1,"wait time:",wait_time)
#     time.sleep(wait_time)
#     wait_time*=2
#     attemps+=1


