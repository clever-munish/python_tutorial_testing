f = open("Demo.txt")
data = f.read()
print(f.name)
print(f.mode)
print(f.closed)
f.close()
print(f.closed)
# datanew = f.read()
# print(datanew)
