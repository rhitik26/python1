#write to a file
#old data gets overwritten so write "a"-apend instead of "w"-write
#fo = open('demo.text', 'w')
fo = open('demo.text', 'a')
fo.write("Hello Superman \n")
fo.write("Hello Batman \n")
fo.write("Hello saurav \n")
fo.close()

with open('demo.text', 'a') as fo:
    fo.write("Hello Superman \n")
    fo.write("Hello Batman \n")
    fo.write("Hello saurav \n")
#with ---no need to close it

#read a file
fo = open('demo.text', 'r')
data=fo.read()
print(data)
fo.close()

fo = open('demo.text', 'r')
print("First:",fo.read(5)) #reads first 5 characters
print("Second:",fo.read(5)) #reads next 5 characters
print("Third:",fo.read(5)) #reads next 5 characters
fo.close()


#reading line by line
fo = open('demo.text', 'r')
print("First:",fo.readline()) #reads first line
print("Second:",fo.readline()) #reads next line
print("Third:",fo.readline()) #reads next line
print(type(fo))
fo.close()

#print by line by line
fo = open('demo.text', 'r')
for line in fo:
    print(line)
fo.close()

#if you want read and write together write----
#r+ or w+ or a+
#all this methods will work on txt based file

#rb, wb, ab--- will read all kinds of file

fo = open('demo.text', 'rb')
for line in fo:
    print(line)
fo.close()

#converting bytes to string

fo = open('demo.text', 'rb')
for line in fo:
    print(line.decode(),end="")
fo.close()
#for reverse write line.encode()

#writing in byte
fo = open('demo.text', 'wb')
fo.write("Hello Superman \n".encode())
fo.write("Hello Batman \n".encode())
fo.write("Hello saurav \n".encode())
fo.close()