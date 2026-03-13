# 
# for i in range(1,5):
#     if i == 3:
#         break
#     print(i)

# for i in range(1,5):
#     if i == 3:
#         continue
#     print(i)

# for i,j in zip(range(1,6),range(5,0,-1)):
#     if i == 3 and j == 3:
#         continue
#     print(i,"",j)

# username = ""
# password = ""
# while username != "Kohana" and password != "1234":
#     username = input("Enter Username :")
#     password = input("Enter password :")

# n=int(input("Enter number:"))
# sum=0
# i=1
# while i<=n:
#     sum=sum+i
#     i=i+1
#     print("The sum of first",n,"numbers is :",sum)

# name = "Kohana"
# newname = ""
# for i in name :
#     if i not in newname:
#         newname += i
# print(name)
# print(newname)
# print(name[::-1]) # reversing a string

# mycart = [10,20,200,300,800,60,700]
# for i in mycart :
#     if i>400:
#         print("This  is my purchased cart item")
#         continue
#     print(i)

# Write a program to check if a given string is palindrome.
# name = input("Enter String:")
# if name == name[::-1]:
#    print("palindrome string")
# else:
#    print("not palindrome")

# write a program to check if two strings are anagraphs of each other
# name = "listen"
# name1 = "silent"
# if sorted(name) == sorted(name1):
#    print("This ia an anagraph")
# else:
#    print("This is not an anagraph")  

# write a function to add key value pairs to a dictionary 
# def add_pair(d, key, value):
#     d[key] = value
#     return d
# mydict = {}
# k = input("Enter first key:")
# v = input("Enter second key:")
# mydict = add_pair(mydict,k,v)
# print(mydict )

# nested for loop
# for i in range(1,4): #outer loop => rows
#     for j in range(1,4): #inner loop => columns
#         print(i,end="")
#     print()

# n=int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(chr(64+i),end="")
#     print()

# n = int(input("Enter the number of rows:"))
# for i in range(1,n+1):
#     for j in range(1,n+1):
#         print(n+1-i,end= " ")
#     print()

n=int(input("Enter the number of rows:"))
for i in range(1,n+1):
    for j in range(1,n+2-i):
        print("*",end= " ")
    print()