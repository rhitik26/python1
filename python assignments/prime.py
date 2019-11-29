number=int(input("Enter the number"))
if number==1:
    print("Not prime")
i=2

flag=0
while i<=number:
    if number%i==0:
        flag+=1
    i+=1
   
if(flag==1):
    print("number is prime")
else:
    print("number is not prime")