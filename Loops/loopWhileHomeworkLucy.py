#1. Write a program to construct the following pattern.
asterics = "*"
while asterics < "******":
    print(asterics)
    asterics = asterics + "*"
    if asterics == "******":
        break
asterics = "*****"
while asterics > "*":
    print(asterics)
    #asterics = asterics - "*" # NEED TO UNDERSTAND - "*"
    #Corrections:
    # 1. Write a program to construct the following pattern.
    count = 1
    length = 5
    symbol = "* "
    while count < length:
        print(count * symbol)
        count += 1

    while count > 0:
        print(count * symbol)
        count -= 1


#Write a program to print alphabet pattern 'O'// IT dRaWS 0 but 1 while is used

#character = "*"
#Easier with For :)
character = "*"
print("", character, "")
for i in range(4):
    print(character, "", character)
print("", character, "")

#CORRECTIONS:
# character = "* "
# count = 8
# print(count//2*" " + character + count//2*" ")
# for i in range(count):
#     print(character + (count-2)*" " + character)
# print(count//2*" " + character + count//2*" ")
character = "* "
count = 8
index = 0

print(count//2*" " + character + count//2*" ")
while index < count:
    print(character + (count-2)*" " + character)
    index += 1
print(count//2*" " + character + count//2*" ")




#2. Write a program to create the multiplication table (from 1 to 10) of a number.
number = int(input("Input a number: "))
multiplier = 1
while multiplier <=10:
    print(number, "*", multiplier, "=", number * multiplier)
    multiplier += 1




#4. Calculate the sum of all numbers from 1 to a given number from user

number = int(input("Enter a number: "))
result = 0
for i in range(1, number + 1):
    result = result+i
print("Result is: ", result)

