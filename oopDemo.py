#classes are user defined blueprint or prototype
#classses have methods functions, methods, class variables instance variables and constructors
#when functions are used in class are called as methods


class calculator:
    num = 100

    def __init__(self,a ,b):
        self.first_number = a
        self.second_number = b
        print("I am called automatically once the object is created ")

    def getData(self):
        print("I am now executing a method inside the class")

    def summation(self):
        return self.first_number + self.second_number + calculator.num

obj = calculator     #syntax to create a object of the class

obj.__init__(calculator ,2,3)
obj.getData(calculator)
print(obj.summation(calculator))
print(obj.num)

obj.__init__(calculator ,4,5)
obj.getData(calculator)
print(obj.summation(calculator))
print(obj.num)
