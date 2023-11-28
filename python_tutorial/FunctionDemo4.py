#how to call a function how to pass a parmenter
# def check_even_number(num):
#     result = num % 2 == 0
#     print(result)
#
#
# check_even_number(10)

def check_odd_number(list1):
    # even_number = []
    odd_number = []

    for x in list1:
        if x % 2 == 0:
            pass
        else:
            odd_number.append(x)
    return odd_number


result = check_odd_number([1, 5, 4, 6, 8])
if len(result) > 0:
    print(result)
else:
    print("Sorry no odd number found")
