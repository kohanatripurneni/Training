# def msg():
#     print("Hello world")
# msg()

# def add():
#     n1 = int(input("Enter the value of n1:"))
#     n2 = int(input("Enter thr value of n2:"))
#     print("Add=",n1+n2)
# add()

# def add():
#      n1 = int(input("Enter the value of n1:"))
#      n2 = int(input("Enter thr value of n2:"))
#      sum = n1+n2
#      mul = n1*n2
#      sub = n1-n1 
#      div = n1/n2
#      return sum,mul,div,sub
# result = add()
#print(result)

#positional arguement
# def personalInfo(fname, lname):
#     print("First Name=", fname)
#     print("Last Name=", lname)
# personalInfo("Kohana","Tripurneni")

# keyword arguement
# def personalInfo(fname, lname):
#     print("First Name=", fname)
#     print("Last Name=", lname)
# fname = "Kohana"
# lname = "Tripurneni"
# personalInfo(fname,lname)

#default arguement
# def cityName(city):
#     print(city)
# cityName("Mumbai")
# cityName("Delhi")
# cityName("Pune")

# variable length arguement
# def studentNames(*name):
#     print(name)
# studentNames("Kohana","Aditi","Janhavi","Kanak")

mylist = [5,2,9,7,5,6]
def searchElement(target):
 for i in range(len(mylist)):
    if target == mylist[i]:
        return i 
    return -1
result = searchElement(10)
if result != -1:
   print("element found at index number =",result)
else:
   print("Element not found")
