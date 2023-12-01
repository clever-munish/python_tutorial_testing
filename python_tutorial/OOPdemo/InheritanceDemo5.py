class BaseClass:
    def hello_Munish(self):
        print("Hello python from base")

    def bye(self):
        print("Bye from python")


class ChildClass(BaseClass):
    def hello_Munish(self):
        super().hello_Munish()
        super().bye()
        # BaseClass.hello_Munish(self)
        print("Hello python from child")


obj1 = ChildClass()
obj1.hello_Munish()
