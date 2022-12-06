# 1. Write a program to check a dictionary is empty or not
myDict = {"key1": "value1", "key2": "value2", "key3": "value3"}
if (len(myDict) == 0):
    print("List is empty")
else:
    print("List is NOT empty")
# Another solution required//

# 2. Write a program to get the top three items in a shop. Go to the editor
# Sample data: {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}
# Expected Output:
# item4 55
# item1 45.5
# item3 41.3
# shoppingItems = {'item1': 45.50, 'item2':35, 'item3': 41.30, 'item4':55, 'item5': 24}

# 3. Write a program to reverse a tuple
myTuple = (1, 2, 3, 4, 5, 6, 7,)
result = reversed(myTuple)
result = tuple(result)
print(result)

# 4. Write a program to convert a tuple of string values to a tuple of integer values. Go to the editor
# Original tuple values:
# ('333', '33', '1416', '55')
# New tuple values:
# (333, 33, 1416, 55)
strTuple = ('1', '2', '3', '4', '5', '6', '7')
intTuple = tuple(int(element) for element in strTuple)
print("Original tuple values: ", strTuple)
print("My Integer Tuple is:", intTuple)


# 5. Write a program to find maximum and the minimum value in a set without min max functions