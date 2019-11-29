def outer(a):
    def inner(*args,**kwargs):
        print("this is inner!")
        print(type(a))
        a(*args,*kwargs)
    #funtion a() and  inner() will become the generic function as both *args and
        # *kwargs are added as parameters so it will accept any number of arguments.

        print("Inner finished execution!")
    return inner
@outer  #By adding this annotation the function will automatically become wrapper function(the concept is Decorator)
def hello(name):
    print("hello "+name)
@outer
def sayhi(name1,name2):
    print("hi "+name1+" "+name2)
#demo1=outer(hello)       #  function hello is the wrapper function of sayhi,
#demo2=outer(sayhi)
hello("Sachin")
sayhi("Sachin","Rahul")
