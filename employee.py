import datetime

class Employee:

    def __init__(self, firstname: str, lastname: str, startDate: datetime.date, salary: int, department: str, prevID: int):
        self._firstname: str = firstname
        self._lastname: str = lastname
        self._startDate: datetime.date = startDate
        self._salary: int = salary
        self._department = department
        self._empId: int = prevID+1

    @staticmethod
    def fromDict(inpDict: dict):
        firstname: str = inpDict['firstname']
        lastname: str = inpDict['lastname']
        startDate: datetime.date = inpDict['startDate']
        salary: int = inpDict['salary']
        department = inpDict['department']
        empId: int = inpDict['empId']
        return Employee(firstname,lastname, startDate, salary, department, empId-1)
    def __eq__(self,other):
        if type(other) == Employee: return self.empId == other.empId
        else: return False

    def __repr__(self):
        return f"{self.empId}: {self.firstname} {self.lastname}\n{self.department} ${self.salary} {self.startDate}"

    def toDict(self) -> dict:
        return {"firstname": self.firstname,
                "lastname": self.lastname,
                "startDate": self.startDate,
                "salary": self.salary,
                "department": self.department,
                "empId": self.empId}

    @property
    def firstname(self) -> str:
        return self._firstname

    @firstname.setter
    def firstname(self, value: str):
        self._firstname = value.lower().capitalize()

    @property
    def lastname(self) -> str:
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        self._lastname = value.lower().capitalize()

    @property
    def startDate(self) -> datetime.date:
        return self._startDate

    @startDate.setter
    def startDate(self, value: datetime.date):
        self._startDate = value

    @property
    def salary(self) -> int:
        return self._salary

    @salary.setter
    def salary(self, value: int):
        self._firstname = value

    @property
    def department(self) -> str:
        return self._department

    @department.setter
    def department(self, value: str):
        self._firstname = value

    @property
    def empId(self) -> int:
        return self._empId

    @empId.setter
    def empId(self, value):
        self._empId = value
