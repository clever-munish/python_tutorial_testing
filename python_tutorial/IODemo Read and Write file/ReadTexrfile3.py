# filePath=os.getcwd()
# try:
#     f = open("Demo.txt")
#     data = f.read()
# except Exception as err:
#     print("Exception is ", err)
# finally:
#     f.close()

import os

filePath = os.getcwd()

with open(os.path.dirname(os.getcwd()) + "\\Demo.Newtxt") as f:
    print("Current state is ", f.closed)
    data = f.read()
    print(data)

print("State of the file is ", f.closed)
