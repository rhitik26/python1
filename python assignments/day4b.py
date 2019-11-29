def outer(a):
    def inner():
        print("this is inner!")
        print(type(a))
        a()
        print("Inner finished execution!")
    return inner
@outer  #By adding this annotation the function will automatically become wrapper function(the concept is Decorator)
def hello():
    print("hello World!")
@outer
def sayhi():
    print("hi world!")
#demo1=outer(hello)       #  function hello is the wrapper function of sayhi,
#demo2=outer(sayhi)
hello()
sayhi()
