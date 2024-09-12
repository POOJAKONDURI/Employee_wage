import random

class Employee:
    def __init__(self,name,wage_per_hour,total_hours,is_part_time=False):
        self.name = name
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.total_hours = total_hours
        self.is_part_time = is_part_time

    def attendance_check(self):
        attendance = random.randint(0,1)
        if attendance == 1:
            work_hours = 4 if self.is_part_time else self.total_hours
            daily_wage = self.wage_per_hour * work_hours
            return f"{self.name} is present and {daily_wage} is daily wage"
        else:
            return f"{self.name} is absent"
        
        
def main():
    name = input("Enter the Name of Employee: ")
    is_part_time_input = input("Is the employee part-time? (yes/no): ").strip().lower()
    is_part_time = True if is_part_time_input == "yes" else False
    part_time = Employee(name,20,8,is_part_time)
    print(part_time.attendance_check())

if __name__ == "__main__":
    main()

