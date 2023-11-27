# range method in for loop

# for x in range(1,101):
# print(x)

# for x in range(30):
# print(x)

# mod % opreator for even and odd number

evenlist = []
oddlist = []

for x in range(50):
    if x % 2 == 0:
        evenlist.append(x)
    else:
        oddlist.append(x)
print(evenlist)
print(oddlist)
