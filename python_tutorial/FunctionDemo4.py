# def check_even_number(num):
#     result = num % 2 == 0
#     print(result)
#
#
# check_even_number(10)

def check_even_number(list1):
    even_number = []
    odd_number = []

    for x in list1:
        if x % 2 == 0:
            pass

        else:
            odd_number.append(x)
    return odd_number


result = check_even_number([1,5,4,6,8])
print(result)

if len(result) > 0:
    print(result)

else:

 print("Sorry no odd number found")
