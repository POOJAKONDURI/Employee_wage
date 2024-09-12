import random

class Employee:
    def __init__(self,name,wage_per_hour,total_hours):
        self.name = name
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.total_hours = total_hours

    def attendance_check(self):
        attendance = random.randint(0,1)
        if attendance == 1:
            daily_wage = self.wage_per_hour * self.total_hours
            return f"{self.name} is present and {daily_wage} is daily wage"
        else:
            return f"{self.name} is absent"
        
def main():
    employe1 = Employee("john",8,20)
    print(employe1.attendance_check())

if __name__ == "__main__":
    main()
