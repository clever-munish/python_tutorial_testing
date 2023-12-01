name = ['Munish', 'Rohit', 'Harish']
marks = [50, 60, 40]
address = ['ABC', 'EFG', 'XYZ']

data = zip(name, marks, address)
# print(data)
mydata = list(data)

a, b, c = zip(*mydata)
print(a)
print(b)
print(c)
