import random

class Employee:
    # Class variables
    wage_per_hour = 20
    full_day_hours = 8
    part_time_hours = 4
    max_working_hours = 100
    max_working_days = 20
    
    def __init__(self, name, is_part_time=False):
        self.name = name
        self.is_part_time = is_part_time
        self.total_working_hours = 0
        self.total_working_days = 0
        self.total_wage = 0
   
    def attendance_check(self):
        """ UC1: Check if employee is present or absent """
        return random.randint(0, 1)

    @classmethod
    def calculate_daily_wage(cls, is_part_time):
        """ UC2 & UC3: Calculate daily wage based on full-time or part-time """
        if is_part_time:
            return cls.wage_per_hour * cls.part_time_hours
        else:
            return cls.wage_per_hour * cls.full_day_hours

    @classmethod
    def calculate_monthly_wage(cls, employee):
        """ UC6: Calculate wages until total working hours or days is reached """
        while employee.total_working_hours < cls.max_working_hours and employee.total_working_days < cls.max_working_days:
            attendance = employee.attendance_check()
            if attendance == 1:
                employee.total_working_days += 1
                if employee.is_part_time:
                    daily_hours = cls.part_time_hours
                    daily_wage = cls.calculate_daily_wage(True)
                else:
                    daily_hours = cls.full_day_hours
                    daily_wage = cls.calculate_daily_wage(False)

                employee.total_working_hours += daily_hours
                employee.total_wage += daily_wage

                print(f"Day {employee.total_working_days}: {employee.name} is Present. Wage: {daily_wage} rupees. Hours Worked: {daily_hours} hours.")
            else:
                employee.total_working_days += 1
                print(f"Day {employee.total_working_days}: {employee.name} is Absent. Wage: 0 rupees. Hours Worked: 0 hours.")

        print(f"\nTotal working hours: {employee.total_working_hours} hours.")
        print(f"Total working days: {employee.total_working_days} days.")
        return employee.total_wage

    @classmethod
    def process_choice(cls, employee, choice):
        """ UC4: Simulate switch-case using class method and variables """
        match choice:
            case 1:
                print(f"{employee.name} is {'Present' if employee.attendance_check() == 1 else 'Absent'}.")
            case 2:
                if employee.attendance_check() == 1:
                    full_day_wage = cls.calculate_daily_wage(False)
                    print(f"{employee.name} is Present. Full-time wage: {full_day_wage} rupees.")
                else:
                    print(f"{employee.name} is Absent. No wage today.")
            case 3:
                if employee.attendance_check() == 1:
                    part_time_wage = cls.calculate_daily_wage(True)
                    print(f"{employee.name} is Present. Part-time wage: {part_time_wage} rupees.")
                else:
                    print(f"{employee.name} is Absent. No wage today.")
            case 4:
                total_wage = cls.calculate_monthly_wage(employee)
                print(f"\nTotal wage for the month: {total_wage} rupees.")
            case _:
                print("Invalid choice! Please select a valid option.")


def main():
    employee = Employee("John Depp") 

    while True:
        print("""
        Menu:
        1. Check Employee Attendance
        2. Calculate Full-Time Employee Wage
        3. Calculate Part-Time Employee Wage
        4. Calculate Wages Until Total Hours or Days Reached
        """)
        
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit():
            choice = int(choice)
            Employee.process_choice(employee, choice)
        else:
            print("Invalid input. Please enter a valid number.")
            continue

if __name__ == '__main__':
    main()
