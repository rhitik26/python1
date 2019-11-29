class person:
    nationality="India"
    def sayhi(self):
        print("Hi "+self.fname+" "+self.lname)
    def __init__(superman,fname,lname):
        superman.fname=fname
        superman.lname=lname

class employee(person):
    org="DXC"
    def __init__(superman,fname,lname,dept,loc):
        person.__init__(superman, fname, lname)
        superman.dept=dept
        superman.loc=loc

    def work(obj):
        print(obj.fname+" is working!")

class student(person):
    institute="Python University"
    def __init__(self,fname,lname,stream):
        person.__init__(self,fname,lname)
        self.stream=stream
    def study(self):
        print(self.fname+" is studying!")

class intern(student,employee):
    def __init__(self,fname,lname,dept,loc,stream):
        student.__init__(self,fname,lname,stream)
        employee.__init__(self,fname,lname,dept,loc)


class manager(employee):
    def __init__(self,fname,lname,dept,loc,reportees):
        employee.__init__(self,fname,lname,dept,loc)
        self.repotees=reportees
    def manage(self):
        print(self.fname+" is managing!")

e1=intern("Sachin",
          "Tendulkar",
          "batting",
          "Mumbai",
          "Sports")

e1.study()
e1.sayhi()

#print(e1.org,e1.nationality,e1.dept,e1.loc)
print(e1.__dict__)

print(employee.__bases__)
print(person.__bases__)