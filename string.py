# firstname="raj"
# lastname="kumar"
# name=firstname +" "+lastname
# print(name)
# print(len(name))

# print(name[1])

# # slicing , in slicing ending is excluded
# print(name[2:5])

# random="raj$kumar$gupta"
# print(random.count("$"))


# conditional statement
# marks=int(input("Enter the marks:"))
# if(marks>=90):
#     print("A")
# elif(marks>=80):
#     print("B")
# elif (marks>=70):
#     print("C")
# else:
#     print("D")

# num=int(input("Enter the number:"))
# if(num%2==0):
#     print("The given number is even")
# else :
#     print("the given number is odd")

name=input("Enter the name:")
original=name
rev=name[::-1]
print(rev)

if original==rev:
    print("the given string is palindrom")

else:
    print("the given string is not palidrome")
