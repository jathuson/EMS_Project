import employeeIO
import employee
import csv
from datetime import date

print("running test on write employee")

csvFile = open("employees.csv", "w")
fieldnames = ['firstName', 'lastName', 'startDate', 'salary', 'department', 'empId']
write = csv.DictWriter(csvFile, fieldnames=fieldnames)
write.writeheader()
csvFile.close()



firstEMP = employee.Employee("s", "kelly", date.today(), 45000, "QA", 0 )
employeeIO.writeNewEmployee(firstEMP)
print(firstEMP.toDict())
