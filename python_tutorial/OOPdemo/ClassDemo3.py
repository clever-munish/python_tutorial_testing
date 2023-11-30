# Constructor will invoke once you create object

# self is just a keyword not something re keyword  some random string i have given

class Person:
    def __init__(self, f, l):
        self.fname = f
        self.lname = l
        print("Hello " + self.fname + " " + self.lname)

    def sum(self, x, y):
        self.v1 = x
        self.v2 = y

        return self.v1 + self.v2


x = Person("Munish", "Verma")
print(x.sum(25, 75))
