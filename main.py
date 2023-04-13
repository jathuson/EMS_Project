from department import Department

print(Department("Marketing", 10000,"123-456-7890"))
inpDict1 = {"name": "Marketing", "budget": 10000, "phone":"123-456-7890"}
print(Department.fromDict(inpDict1))