#Approach 1 :using the temporary variable

myList = [12, 23, 54, 25]
size = len(myList)

temp=myList[0]
myList[0]=myList[size-1]
myList[size-1]=temp

print("list after swapping is", myList)