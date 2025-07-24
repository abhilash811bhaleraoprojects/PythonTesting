#file = open('test.txt')
#print(file.read())   #will read whole file
#print(file.read(5))  #this will read n number of characters by passing parameters

#print(file.readline())  # read one single line at a time using readline method





#write a program to read line by line using readline method
file = open('test.txt')
line = file.readlines()
#while line != "":
#    print(line)
#    line = file.readline()

for line in file.readlines():
    print(line)



file.close()