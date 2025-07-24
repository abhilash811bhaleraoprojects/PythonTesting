str = "Abhilashbhalerao.com"
str1 = "Software tester"
str2 = "Abhilash"

print(str[2])
print(str[0:8])
print(str + " " +  str1)

print(str2 in str)
print(str2 in str1)

#split method
var = str.split(".")  #this method will separate the string based on the given condition
print(var)
print(var[0])

#strip method
#this will trim the void spaces in a string in the beginning or at the end

str4 = "  great  "
print(str4.strip())  #will remove the void spaces from both sides
print(str4.lstrip())  #will remove the void spaces from left side of the string
print(str4.rstrip())  #will remove the void spaces from right side of the string