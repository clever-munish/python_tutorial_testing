try:
    f = open("Demo.txt")
    data = f.read()
except Exception as err:
    print("Exception is ", err)
finally:
    f.close()
