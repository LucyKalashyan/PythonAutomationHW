
myName = "Lusine Kalashyan"
print(len(myName))
print(myName[9])
print(myName[:10])
print(myName[2:])
print(myName[0:-10])
print(myName[0:12:2])






#01. Write a program to print odd index elements in a list
myNumList = [1,2,3,4,5,6,7,8,9,10,11,12,13]
print(myNumList[0:13:2])




#02. Write a program to get the largest number from a list

largestNumber = [1,5,9,12,80,100]
print(max(largestNumber))

# another version
myNumList = [1,4,2,6,184,3,8,2,78,1,9,7]
myNumList.sort()
print(myNumList[-1])






#03. Write a program to remove duplicates from a list
myNumList = [1,2,3,4,5,1,2]
print(list(set(myNumList)))

#another example
myList = ["high", "low", "average", "high", "low"]
print(list(set(myList)))





#04. Write a program to convert a string to a list

myString = "I love to make cakes"
print(myString.split())






#05.Write a program to find the item with maximum occurrences in a given list
myList = "Apple","Kiwi","Banana","Kiwi","Orange","Pear","Kiwi","Apple", "Pineapple"
maxOccurence = max(myList, key = myList.count)
print("The word with maximum occurences is :", maxOccurence)





#06. Write a program to check whether a specified list is sorted or not
myList =[1,6,2,7,3,8,4,9,5,0]
print("My List is sorted: ", myList)