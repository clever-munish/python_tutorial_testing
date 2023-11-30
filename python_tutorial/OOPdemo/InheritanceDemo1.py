class Base:
    name = "Munish"

    def baseMethod(self):
        print("I am in BaseClass")


class Child(Base):
    company = "Chd"

    def childMethod(self):
        print("I am child class")


c = Child()
c.childMethod()
c.baseMethod()
print(c.name)
print(c.company)
