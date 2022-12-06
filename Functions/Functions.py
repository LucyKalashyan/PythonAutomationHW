#1. Write a function to multiply all the numbers in a given list
def my_List (my_num):
    startNum = 1
    for item in my_num:
        startNum *= item
    return startNum
print("List number multiplication is : ", my_List((2,3,2)))

#2. Write a function that takes a list and returns a new list with unique elements of the first list
def my_list(unique_list):
  start = []
  for element in unique_list:
    if element not in start:
      start.append(element)
  return start
print("Unique elements are : " , my_list([1,2,2,3,4,4,5,5,6,7,8]))

#3. Write a function to print the even numbers from a given list.
def even_num(my_num):
    start = []
    for element in my_num:
        if element % 2 == 0:
            start.append(element)
    return start
print("Even numbers are: ", even_num([1,2,3,4,5,6,7,8]))

#4. Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def case_count(my_str):
    uppercase_count = sum(1 for char in my_str if char.isupper())
    lowercase_count = sum(1 for char in my_str if char.islower())
    print("Uppercase characters: %s" % (uppercase_count))
    print("Lowercase characters: %s" % (lowercase_count))
case_count("Python is mind-blowing,I love it!")

#Another solution:BUT, needs to have separate results:(
def case_count(my_str):
    upper_case = 0
    lower_case = 0
    for char in my_str:
        if char.islower():
            lower_case += 1
        elif char.isupper():
            upper_case += 1
    return(upper_case, lower_case)
print(case_count("Python is mind-blowing,I love it!"))

#5.Write a Python function that takes a number as a parameter and check the number is prime or not
def my_num(prime):

