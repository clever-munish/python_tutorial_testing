# while with Else, Break, Continue and Pass

# expample with Break

num = 11
while num < 15:
    print(num)
    num = num + 1
    if num == 10:
        print(num)
    break
else:
    print("Condition is not true")
