#Anonymous function
#Inline function
#lambda function

"""
Rule1:Function should contain only one line
Rule2:that 1 line should be return statement

def sayhi(n1,n2):
    return ("hi "+n1+" "+n2)
    data=(lambda n1,n2: "Hi "+n1+" "+n2)("Sachin","Rahul")
print(data)
"""
hello=lambda n1,n2: "Hi "+n1+" "+n2
print(type(hello))
print(hello("A","B"))
print(hello("C","D"))
print(hello("E","F"))

add=lambda n1,n2: n1+n2
print(add(10,20))