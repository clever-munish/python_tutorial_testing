# Multilevel Inheritance
class classA:
    def methodA(self):
        print("I am coming from Chd")

    def hello_Munish1(self):
        print("Hello from class A ")


class classB:
    def methodB(self):
        print("I am coming form class B")

    def hello_Munish2(self):
        print("Hello from class B ")


class classC(classA, classB):
    def methodC(self):
        print("I am coming form class C")


c = classC()
c.methodA()
c.methodB()
c.methodC()
c.hello_Munish1()
c.hello_Munish2()
