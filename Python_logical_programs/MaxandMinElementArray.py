#input : arr[1, 2, 3, 4, 5]
#output for max : 5
#output for min : 1

lis = [20, 54, 76, 70]

max = lis[0]
n = len(lis)

for i in range(1,n):
    if lis[i] > max:
        max = lis[i]

print(max)



# to print the min element

lis = [10, 90, 76, 80]

min = lis[0]
n = len(lis)

for i in range(1,n):
    if lis[i] < min:
        min = lis[i]

print(min)