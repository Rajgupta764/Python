
# classes the the blues print for creating the objects
# object is the instaces of the class

# class student:
#     name="raj kumar ",
#     age=20,
#     cgpa=9.0,
#     rollno=127

# st=student()
# print(st.age)

#learning concept of oops in python


# class studetn:
#     def __init__(self,name,age):
#         self.name=name
#         self.age=age
        

# s1=studetn("raj",20)
# print(s1.age)
# print(s1.name)

class student:
    def __init__(self,maths,dsa,java):
        self.maths=maths
        self.dsa=dsa
        self.java=java

    def avg(self):
        average=(self.dsa+self.maths+self.java)/3
        print("the avg of the given marks is :",average)

s1=student(80,98,96)
s1.avg()