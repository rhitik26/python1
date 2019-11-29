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
#--------------------------------------------------
def mysort(el):
    print("mysort called for "+el['fname'])
    return el["fname"]
ob.sort(key=mysort)
print(ob)
#--------------------------------------------------

