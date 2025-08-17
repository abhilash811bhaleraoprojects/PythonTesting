#Approach 1 :using the temporary variable

myList = [12, 23, 54, 25]
size = len(myList)

temp=myList[0]
myList[0]=myList[size-1]
myList[size-1]=temp

print("list after swapping is", myList)

#Approach 2
myList = [12, 23, 54, 25]
myList[0], myList[-1] = myList[-1], myList[0]
print("list after swapping is using approach 2", myList)
