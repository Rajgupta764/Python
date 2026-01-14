# def factorial(n):
#     fact=1
#     for i in range(1,n+1):
#         fact=fact*i

#     print("the factorial of the given number is :",fact)

# factorial(5)

# currency converter
# sum=0
# def additon(n):
#     if(n==0):
#         return 1
#     else:
#         return n+additon(n-1)

# result=additon(10)
# print(result)


def fact(n):
    if(n==0 | n==1):
        return 1
    else:
        return n*fact(n-1)

print("the factorial of the given number is :",fact(5))
