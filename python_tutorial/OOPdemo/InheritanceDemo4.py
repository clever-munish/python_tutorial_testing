# # mro Method overriding in python
#
# what is method override ?
# Ans: - When Parent Class and Child class has the same method with same signature,in that case
# child class override the same method of Parent class.

class A:
    def sum(self):
        print("calling form A-sum of 2 number is 15")


class B(A):
    def sum(self):
        print("calling form B-sum of 2 number is 25")


class C(B):
    def sum(self):
        print("calling form C-sum of 2 number is 50")


obj1 = A()
obj1.sum()

# obj1 = A()
# obj1.sum()
#
# obj2 = B()
# obj2.sum()
