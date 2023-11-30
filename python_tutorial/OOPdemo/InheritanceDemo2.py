# Multilevel Inheritance
class A:
    def methodA(self):
        print("I am coming from class A")

    def hello_Munish(self):
        print("hello i am form Class A")


class B(A):
    def methodB(self):
        print("I am coming from class B")


class C(B):
    def methodC(self):
        print("I am coming form class C")


class D(C):
    def methodD(self):
        print("I am coming form class D")


obj1 = D()
obj1.methodA()
obj1.methodB()
obj1.methodC()
obj1.methodD()
obj1.hello_Munish()
