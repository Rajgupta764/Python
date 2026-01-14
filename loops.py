# num=0
# while(num<40):
#     print(num)
#     num=num+1


# days=int(input("Enter the days:"))
# match days:
#     case 1: print("monday")
#     case 2: print("tuesday")
#     case 3: print("wednesday")
#     case 4: print("thursday")
#     case 5: print("friday")
#     case 6: print("saturday")
#     case 7:print("sunday")
#     case _:
#         print("invalid day ")

# print the number in descending order 
# num=100
# while(num>0):
#     print(num)
#     num=num-1


list=[1,2,3,4,5,6,7,8]
for num in list:
    if(num==5):
        continue
    # print(num)

# for number in range(1,5,2):
#     print(number)


# sum of first n natural number 
n=int(input("Enter the value of n:"))
# def sum(n):
#     sums=n*(n+1)/2
#     print("the sum of the given number is :",sums)


# sum(n)
# sum=0
# while(n>0):
#     sum=sum+n
#     n=n-1
# print(sum)

fact=1
for i in range(1,n+1):
    fact=fact*i

print("the factorial of the given number is :",fact)

        



