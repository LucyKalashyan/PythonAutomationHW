#1. Write a Python program that accepts a word from the user and reverse it.
#word = str(input("Enter a word: "))
#reverse = str(input(word[::-1]))

#CORRECTIONS SEE BELOW:
#word = input("Enter a word: ")
#reverse = word[::-1]
#print(reverse)




#2. Write a Python program to count that user inputed number is even or odd.
#number = int(input("Please enter a number: "))
#remainder = number % 2
#if remainder > 0:
    #print("It's an ODD number!")
#else:
    #print("It's an EVEN number!")

#MINE IS RIGHT BUT THIS ONE USES JUST 1 VARIABLE// EASIER, BETTER

#number = int(input("Please enter a number: "))
#if number % 2 != 0:
    #print("It's an ODD number!")
#else:
    #print("It's an EVEN number!")





#3. Write a Python program to find the inputed number from 100 to 400 (both included).
#THIS ON E IS CORRECT!
#number = int(input("Enter a number: "))
#if number >= 100 and number <= 400:
   # print("It is included!")
#else:
    #print("It is NOT included!")





#4. Write a Python program to get next day of a given date.
year = int(input("Input a year: "))
month = int(input("Input a month [1-12]: "))
day = int(input("Input a day [1-31]: "))
if day >31 or day <1 or month >12 or month<1:
    print("Enter a valid date!") # It works fine
elif month ==12:
    print("Next Date is :", year, month, day +1) # It works fine
elif day ==31 and month !=12:
    print("Next date is: ", year, month +1, day % 2) # It works fine
elif month ==12 and day ==31:
    print("Next date is: ", year +1, month ==1, day ==1) # NOT WORKING!!!!!