# #remove duplicate character from string
# from collections import OrderedDict
# str="aabbhhii"
# words="".join(OrderedDict.fromkeys(str))
# print(words)

# #Show half charater in upper case
# str="abhi"
# length=len(str)//2
# first_half=str[0:length]
# sec_half=str[length:]
# print(first_half.upper()+sec_half)

# #show first and last char in upper
# str="abhibhalerao"
# first=str[0]
# last=str[-1]
# middle=str[1:-1]
#print(first.upper()+middle+last.upper())

#show last word from sentence
# str="abhilash bhalerao pune"
# words=str.split(" ")
# print(words[-1])

# # count digit from string
# str="abhi123"
# sum=0
# for i in str:
#     if i.isdigit():
#         sum=sum+int(i)
# print(sum)

# #calculate frquency of character
# str="aabhhiibbb"
# from collections import Counter
# print(Counter(str))


#displaye vowel from string

# str="abhilashbpune"
# for i in str:
#     if i.lower() in 'aeiou':
#         print(i)

# # Show count of vowels
# str="abhilashbhalerao"
# count=0
# for i in str:
#     if i in 'aeiou':
#         count=count+1
# print(count)


# #remove ith char from string
# str="abhilash"
# k=4
# str_rev=" "
# for i in range(len(str)):
#     if i!=k-1:
#         str_rev=str_rev+str[i]
# print(str_rev)

# #Add space between each word
# str='AbhilashAnandaBhalerao'
# import re
# space=re.findall("[A-Z][a-z]*",str)
# print(space)

# #check pallendrom sring
# str="madam"
# if str==str[::-1]:
#     print("string is palindrome")
# else:
#     print("string is not palindrome")


# #remove dupliacte from string
# str='aabbhhii'
# from  collections import OrderedDict
# words= "".join(OrderedDict.fromkeys(str))
# print(words)

# #count value
# mylist=[1,2,3,4,5,6]
# em_list=[]
# for i in mylist:
#     em_list.append(i)
# print(em_list)

# #check abhilash present or not in list
# str=['abhilash','bhalerao','pune']
#
# if 'abhilash' in str:
#     print("yes present")
# else:
#     print("not preset")

# # add item in list
# str=[1,2,3,4,5]
# index=str.index(4)
# str[index]='abhi'
# print(str)

# # remove duplicate from list
# from  collections import Counter
# list1=[1,2,2,5,5,5,5,3,4,5,6]
# print(Counter(list1))


# #show duplicate and unique from list
# list1=[1,2,3,4,5,1,2,3]
# unique=[]
# duplicate=[]
# for i in list1:
#     if i not in unique:
#         unique.append(i)
#     else:
#         duplicate.append(i)
# print((unique))
# print((duplicate))

#show 2nd max value fromlist
#list1=[1,2,3,4,5,6,7,8,8,9]

# mylist=list(set(list1))
# mylist.sort()
# print(mylist[-2])
#
# list1=[1,2,3,4,5,6,7,8,8,9]
# unique=[]
# for i in list1:
#     if i not in unique:
#         unique.append(i)
# print(unique[-2])

# #
# mytuple=('apple','banana','cherry')
# myt2=list(mytuple)
# myt2.pop(1)
# print(tuple(myt2))
#
# list1=["abhi","bhalerao"]
# list2=["a","b"]
# list3=[]
#
# for i in range(len(list1)):
#     list3.append(list1[i]+list2[i])
# print(list3)
#
# list1=["abhi","bhalerao"]
# list2=["a","b"]
#
# list3=list1+list2
# print(list3)

# # Show duplicate and uniq from list
# list1=[1,2,3,4,51,1,2,3,2,2,4,4,4]
# uniq=[]
# dup=[]
#
# for i in list1:
#     if i not in uniq:
#         uniq.append(i)
#     else:
#         dup.append(i)
# print("uniq value", uniq)
# print("duplicate value",dup)
#
# list1=[1,2,3,4,51,1,2,3,2,2,4,4,4]
# list2=list(set(list1))
# print(list2)

#
# list1=[1,2,3,4,1,2,3]
# mul=[]
# for i in list1:
#     mul.append(i*i)
# print(mul)


# mylis1=['abhi',1]
# mylist2=['bhalerao',2]
# mylist3=dict(zip(mylis1,mylist2))
# print(mylist3)

# str="abhilashbhalerao"
# from collections import OrderedDict
# str2="".join(OrderedDict.fromkeys(str))
# print(str2)
#
# #show max character from string
# str="abhibhalerao"
# print(max(str))
#
#
# #find count or length of string
# string="abhi bhalerao pune"
# print(len(string)) #18
#
# #find character ends with e or not
# print(string.endswith("e")) #true

# convert first character capital
#print(string.capitalize())

# find character index
# print(string.rfind("e"))
# remove e from string
# print(string.replace("e","",1))
# show last character from list
# words=string.split()
# print(words[-2])
# print("*".join(string))
#
# remove only 1st e
# print(string.replace("e","",1))
#
# # remove duplicate from string
# string="pprreemm"
# from collections import OrderedDict
# words= "".join(OrderedDict.fromkeys(string))
# print(words)
# # remove ith char from string
# string="premkatre"
# k=1
# strr=" "
# for i in range(len(string)):
#     if i!=k-1:
#         strr=strr+string[i]
# print(strr)

# show half character in upper
# string="prem"
# length=len(string)//2
# first_half=string[0:length]
# sec_half=string[length::]
# print(first_half.upper()+sec_half)

# # # count digit from string
# string="prem123"
# sum=0
# for i in string:
#     if i.isdigit():
#         sum=sum+int(i)
# print(sum)

# calculate frequency of character
# from collections import Counter
# string="abhibhalerao"
# print(Counter(string))

# # display vowels of string
# string="abhibhalerao"
#
# for i in string:
#     if i not  in 'abhi':
#         print(i)

# count vowels
# string="aeiou"
# count=0
# for i in string:
#     if i in 'aeiou':
#         count=count+1
# print(count)

# add space between character
# import re
# string="AbhiBhalerao"
# words=string.
# print(words)


#
#list1=[10,9,8,7,5,5,2,1]
# list2=list(set(list1))
# print(list2)
# uniq = []
# dup = []
# for i in list1:
#
#     if i not in uniq:
#         uniq.append(i)
#     else:
#         dup.append(i)
# print(uniq)
# print(dup)

# show 2nd max
# list1=[1,70,60,60,60,50,50,4,0,40]
# list1.sort()
# print(list(set(list1)))
# print("second max:-",list1[-2])

# # show odd even value from list
# list1=[10,1,2,3,4,5,6]
# even=[]
# odd=[]
# for i in list1:
#     if i%2==0:
#         even.append(i)
#     else:
#         odd.append(i)
# print(even)
# print(odd)

# swap 1st and last word from list
# list1=[1,2,3,4]
# list2=[1,2,3,4]
# prt=dict(zip(list2,list1))
# print(prt)

# # concatenate two list index wise
# l=[1,2,3,4]
# k=[5,6,7,8]
# h=[]
# for i in range(len(l)):
#     h.append(l[i]+k[i])
# print(h)

# multipy all the number of list
# l1=[1,2,3,4,5,6]
# square=[]
# for i in l1:
#     square.append(i*i)
# print(square)

# remove space from list
# li=[1,"",3]
# print(list(filter(None,li)))



# # show max char from string
# str="abhi"
# v=min(str)
# print(v)

# strp="abhi"
#
#
# print(len(strp))
# print(strp.endswith("i"))
# print(strp.count("e"))
# print(strp.capitalize())
# print(strp.rfind("e"))
# print(strp.split("k"))
# print(" ".join(strp))

# just="verygood"
# k=4
# update=" "
# for i in range(len(just)):
#     if i!=k-1:
#         update=update+just[i]
# print(update)

# remove duplicate character from string
# strew="aabbhhii"
# from collections import OrderedDict
# uniq="".join(OrderedDict.fromkeys(strew))
# print(uniq)




# calculate frequency of charater
# port="abhibhaleraooo"
# from collections import Counter
# print(Counter(port))

# display vowels
vowels="opuietyu"
new_v=""
count=0
for i in vowels:
    if i in 'aeiou':
        print(i)
        count=count+1
print(count)


