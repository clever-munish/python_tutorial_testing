# def print_name(name1, name2):
#     print(name1, name2)
#
#
# print_name("Python", "JAVA")

# tuple var(*args) receive a value as a tuple
def print_name(*args):
    # print(args)
    # print(args[1])
    for name in args:
        print(name)


print_name("Python", "JAVA", "JS", "Ruby")


def get_min_of_all_number(*args):
    print(min(args))


def get_sum_of_all_number(*args):
    print(min(args))


def get_max_of_all_number(*args):
    print(max(args))


get_sum_of_all_number(10, 20, 30, 40)
get_max_of_all_number(90, 40, 50, 60, 96, 85)
get_min_of_all_number(65, 63, 96, 2, 35, 45, 65)
