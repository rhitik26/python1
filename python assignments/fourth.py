def sayhi(n1,n2,n3):
    print("Hi "+n1+' '+n2+' '+n3)

li=["Sachin","Saurav","Rahul"]
li=("Sachin","Saurav","Rahul")    
li={"Sachin","Saurav","Rahul"}
sayhi(*li)


list={
        "n1":"Sachin",
        "n2":"Saurav",
        "n3":"Rahul"
    }
    
sayhi(**list)        