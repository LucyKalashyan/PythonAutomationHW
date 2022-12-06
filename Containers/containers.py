# 1. Write a Python program to get the largest number from a list.
myNumbers = [1, 3, 2, 4, 17, 5, 6, 7, 8, 10]
print(max(myNumbers))

# another solution:
myNumbers = [1, 3, 2, 4, 17, 5, 6, 7, 8, 10]
largestNumber = myNumbers[0]
for item in myNumbers:
    if item > largestNumber:
        largestNumber = item
print("Largest Number is : ", largestNumber)

# 2. Write a Python program to check a list is empty or not.
myList = ["a", "b", "c", "d"]
if len(myList) == 0:
    print("List is empty")
else:
    print("List is NOT empty", myList)

# 3. Write a Python program to remove all elements from a given set.
myElements = {1, 2, 3, 4, 5, 6}
myElements.clear()
print(myElements)

# 4. Write a Python program to check if a given value is present in a set or not.//to do
#mySet = {1, 2, 3, 4, 5}
#if mySet == None:
    #print("The given value is NOT present")
#else:
    #print("The given value is present")

# 5. Write a Python program to convert a list to a tuple.
myList = [11, 12, 13, 14, 15, 16, 17]
myTuple = tuple(myList)
print("Here is my list converted into a tuple:", myTuple)

# another solution:
myList = [11, 12, 13, 14, 15, 16, 17]
print("Here is my list converted into a tuple:", tuple(myList))

# 6. Write a Python program to remove an item from a tuple.
myTupleList = [("a", "b"), ("c", "d"), ("e", "f")]
del myTupleList[1]
print(myTupleList)

# 7. Write a Python script to check whether a given key already exists in a dictionary or not.
myDict1 = {"book1": "chapter1", "book2": "chapter2", "book3": "chapter3"}
if myDict1.get('book5') == None:
    print("The given Value does NOT exist in the dictionary!")
else:
    print("The given Value EXISTS in the dictionary!")

# 8.Write a Python script to merge two Python dictionaries.
dict1 = {"student1": "Anush", "student2": "Artak", "student3": "Valod"}
dict2 = {"teacher1": "Saro", "teacher2": "Marine", "teacher3": "Yeraz"}
dict1.update(dict2)
print("Merged List of 2 Dictionaries:", dict1)
#-------------------------------------------------------------------


