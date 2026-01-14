class A:
    varA="This is my class A"

class B:
    varB="This is my class B" 

class C:
    varc="This is my class C"

class D(A,B,C):
    varD="This is my class D"

d1=D()
print(d1.varA)
print(d1.varB)
print(d1.varc)
print(d1.varD)