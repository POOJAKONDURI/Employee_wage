import random

class Employee:
    def __init__(self,name):
        self.name = name

    def attendance_check(self):
        attendance = random.randint(0,1)
        if attendance == 1:
            return f"{self.name} is present"
        else:
            return f"{self.name} is absent"

employe1 = Employee("john")
print(employe1.attendance_check())
