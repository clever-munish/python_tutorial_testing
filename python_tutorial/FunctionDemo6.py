def print_names(**kwargs):
    print(kwargs)
    print(kwargs["address"])


print_names(name="Munish", address="Chd", phone=9090)


def hello_world(*args, **kwargs):
    print(args)
    print(kwargs)


hello_world(10, 20, 30, name="Pyhton", country="India")

# result 10,20,30 in Tuple and name python and country india in Dictionary
