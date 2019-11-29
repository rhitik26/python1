

ob=[
    {
    "fname":"Sachin",
    "lname":"Tandon",
    "city":"bengaluru"
},
{
    "fname":"Ramu",
    "lname":"kaka",
     "city":"Primecity"
},
{
    "fname":"Rahul",
    "lname":"Dravid",
    "city":"bengaluru"
}
]
"""
#--------------------------------------------------
def mysort(el):
    
    return el["fname"]
ob.sort(key=lambda el:el["fname"])
print(ob)
#-----------
"""
#sort
ob.sort(key=lambda el:el["fname"])
print(ob)

obj=[22,32,19,43]
#map
newobj=map(lambda el:32+el*9/5,obj)


#filter
newobj=filter(lambda el: el["team"]=="India",obj)
