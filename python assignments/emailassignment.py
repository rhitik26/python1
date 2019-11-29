import os.path
import re

#print(os.listdir("C:\\Users\\psrivastav46\\Documents\\python\\demo"))
li=os.listdir("C:\\Users\\psrivastav46\\Documents\\python\\demo")
#print(type(li))
#text="hello priyanshu priyanshu.srivastava@gmail.com"
for i in li:

    net=os.path.splitext(i)
    if(net[1]==".log"):
        print(i)
        f=open("C:\\Users\\psrivastav46\\Documents\\python\\demo\\"+i,"rb")
        data = f.read().decode()
        pattern="\S+@\S+"
        matches=re.findall(pattern,data)
        print(matches)


        f.close()