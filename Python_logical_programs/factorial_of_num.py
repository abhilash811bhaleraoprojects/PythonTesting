fact = 1
num = 5

if num<0:
    print("factorial does not exist for negative number")
elif num == 0:
    print("factorial of 0 is 1")
else:
    for i in range(1,num+1):
        fact = fact * i
    print("the factorial of ", num,"is",fact)