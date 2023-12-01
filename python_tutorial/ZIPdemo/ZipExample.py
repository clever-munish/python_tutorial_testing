# zip function in Python

# print(dir(__builtins__))

# print(zip)

name = ['Munish', 'Rohit', 'Harish', 'Python']
marks = [50, 60, 40, 55]
address = ['ABC', 'EFG', 'XYZ']

data = zip(name, marks, address)
# print(data)
mydata = list(data)
print(mydata)

l1 = [1, 2, 3, 4]
print(list(zip(l1)))
