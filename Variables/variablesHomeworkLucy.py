#1. Write a program to solve (x + y) * (x + y).
      #Test Data : x = 4, y = 3
      #Expected Output : (4 + 3) ^ 2) = 49
x = 4
y = 3
problemSolution = (x + y) * (x +y)
print(problemSolution)





#2. Write a program to parse a string to Float or Integer
number1 = "5"
parseNumber1 = int(number1)
print(number1)
print(type(parseNumber1))

number2 = "7.3"
parseNumber2 = float(number2)
print(number2)
print(type(parseNumber2))




#3. Given variables x=30 and y=20, write a Python program to print "30+20=50" via variables
x = 30
y = 20
print(x, "+",  y, "=", x + y)




#4. Write a program to get the Type, and Value of a variable
myFriend = "Suzan"
print(myFriend)
print(type(myFriend))

friendAge = 35
print(friendAge)
print(type(friendAge))

friendHeight = 180.5
print(friendHeight)
print(type(friendHeight))

isMyFriendClever = True
print(isMyFriendClever)
print(type(isMyFriendClever))




#5. Write a program to get the volume of a sphere with radius 6
# V = 4/3 × π × r3
radius = 6
pi = 3.14
volume = 4/3 * pi * radius * radius * radius
#volume = 4/3 * pi * radius ** 3
result = volume
print(result)
#print("The volume of a sphere with radius 6 ", "=", result)





#6. Write a program to display your details like name, age, address in three different lines
myName = "Ann"
myAge = "25"
myAddress = "Azatutyan Str."
print(myName)
print(myAge)
print(myAddress)




#7. Write a program to count the 7% of 500
number1 = 500
number2 = 7
total = (number1 * number2) / 100
print(total)


