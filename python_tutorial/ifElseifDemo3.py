#print("welcome")
#if 15>10:print("Yes")
#print("Bye")


#print("yes") if 5> 10 else print("NO")

#variable
marks=95
#print("A+") if marks> 90 else print("A")

sal=input("please enter your salary for loan:")
#sal=10000000
if sal>40000:
    print("Eligible for car loan")
    if sal>80000:
        print("eligible for home loan")
        if sal>1000000:
            print("premium customer - eligible for all kind of loan")
else:
    print("sorry we could not serve you")
