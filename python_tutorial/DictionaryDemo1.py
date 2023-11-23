
#multipule key pair we can print

#emp={"QATeam": "Munish","dev":"Rahul","Security":90,50:"Pyhton"}
#print(emp)
#print(emp['dev'])
#print(emp.get("dev"))

emp={"QAteam":("Munish","Rahul","arpit"),"Dev": "Rohit"}
#print(emp["QAteam"][0])
emp1=emp["QAteam"]
#print(emp1[2])

emp={"Qa":"Munish","Dev":{"frontend":"Rahul","backend":"Neha"}}
#print(emp.get("Dev"))
emp1=emp.get("Dev")
emp_name=emp1.get("backend")
print(emp_name)

emp["manager"]="xyz"
print(emp)

#pop remove the value item form the last and first
emp.pop("Qa")
print("****************************")
print(emp)
emp.popitem()
print(emp)

