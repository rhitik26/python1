
f = open("demo.txt", "r")
print("First: ", f.readline())  # first 3 chars
print("Second: ", f.readline())  # next 3 chars
print("Third: ", f.readline())  # next 3 chars
f.close()


f = open("demo.txt", "r")
data = f.read()
print(data)
f.close()

f = open("demo.txt", "r")
for line in f:
    print(line)
f.close()

with open("demo1.txt", "w") as fo:
    fo.write(data)

f = open("demo.txt", "r")
for line in f:
    print(line)
f.close()