number=int(input("Enter the number"))
i=1
c=0
while i<=number:
    if number%i==0:
        c+=1
    i+=1
   
   
print(c)