

#how to convert tuple into List

tup1=(1,"Munish",10.2, True,2,2,2,4,5,6,"QA")
#print(type(tup1))
print(tup1)

l1=list(tup1)
#print(type(l1))
print(l1)

s1=set(tup1)
#print(type(s1))
print(s1)

print("************************")
tup2=("Munish")
print(tup2)
print(len(tup2))

tup3=("Munish","Verma")
print(tup3)
print(len(tup3))

l1=[(1,3,5),(2,4,6),(10,20,30)]
print(l1[1][2])