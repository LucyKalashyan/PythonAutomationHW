#1. Перемножить все не чётные значения в диапазоне от 9173 до 9435;
start = 9173
for i in range(9173,9435):
   if i % 2 != 0:
       start *= i
print(start)

#3. Display numbers from -10 to -1 using for loop
for i in range(-10, 0):
    print(i)



#4. Calculate the cube of all numbers from 1 to a given number from user//not solved
number = int(input("Enter a number: "))
cube = number**3
for i in range(1, cube):
    print("Result is: ", i)

#5. Find the factorial of a given number
number = int(input("Enter a number: "))
startNumber = 0
factorial = startNumber * 1
for i in range(1, factorial):
    print(i)

