class Person:

    def welcome(self):  # method
        print("Hello Python")

    def hello_world(self):
        print("Hello World")

    def sum(self, num1, num2):
        print(num1 + num2)


p = Person()  # object
# p.welcome()
p.name = "Munish"
p.phone = 9685745
p.country = "India"
p.city = "CHD"

q = Person()
q.name = "Rahul"
q.phone = 968572445
q.country = "USA"

print(p.name)
print(q.phone)
print(p.city)

# p.sum(12, 31)
