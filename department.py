
class Department:

    def __init__(self, name: str, budget: int, phone: str):
        self._name = name
        self._budget = budget
        self._phone = phone

    def inDep(self, employeeDict: dict) -> dict:
        employeeList = employeeDict.values()
        inDepartment = [employee for employee in employeeList if employee.department == self.name]
        inDepDict = {}
        for employee in inDepartment:
            inDepDict[employee.empId] = employee.copy()
        return inDepDict

    def __repr__(self):
        return f"{self.name} (${self.budget})\n {self.phone}"
    @staticmethod
    def fromDict(inpDict: dict):
        try:
            name = inpDict["name"]
            budget = inpDict["budget"]
            phone = inpDict['phone']
            return Department(name, budget, phone)
        except KeyError:
            print("Error: Dictionary is not in valid format")
            return False

    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = value

    @property
    def budget(self) -> int:
        return self._budget

    @budget.setter
    def budget(self, value: int):
        self._budget = value

    @property
    def phone(self) -> str:
        return self._phone

    @phone.setter
    def phone(self, value: str):
        self._phone = value
