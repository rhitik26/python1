obj=[
    {"team":"India","fname":"Sachin","lname":"Tendulkar"},
    {"team":"India","fname":"Saurav","lname":"ganguly"},
    {"team":"India","fname":"Shami","lname":"mohd"},
    {"team":"England","fname":"shah","lname":"owais"},
    {"team":"Afghanistan","fname":"Salman","lname":"khan"}]
def myfilter(el):
            return el["team"]=="India"
newobj=filter(myfilter,obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))


    def myfilter(el):
        return el["fname"] == el["fname"].startswith("S")
newobj = filter(myfilter, obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))

newobj = filter(lambda el: el["team"] == "India", obj)
print(type(newobj))
for i in newobj:
    print('{fname} {lname}'.format(**i))