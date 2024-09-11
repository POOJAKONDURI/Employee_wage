import random

class Employee:
    def __init__(self, name, wage_per_hour=20, full_day_hours=8, part_time_hours=4):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = full_day_hours
        self.part_time_hours = part_time_hours

    # UC1: Check if employee is present or absent
    def attendance_check(self):
        attendance = random.randint(0, 1)
        return attendance

    # UC2: Calculate Daily Wage ( full-time employees)
    def calculate_full_day_wage(self):
        return self.wage_per_hour * self.full_day_hours

    # UC3: Add part-time employee and calculate wage
    def calculate_part_time_wage(self):
        return self.wage_per_hour * self.part_time_hours

    # UC4: use switch-case
    def process_choice(self, choice):
        attendance = self.attendance_check()
        match choice:
            case 1:  
                print(f"{self.name} is {'Present' if attendance == 1 else 'Absent'}.")
            case 2:  
                if attendance == 1:
                    full_day_wage = self.calculate_full_day_wage()
                    print(f"{self.name} is Present. Full-time wage: {full_day_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 3:  
                if attendance == 1:
                    part_time_wage = self.calculate_part_time_wage()
                    print(f"{self.name} is Present. Part-time wage: {part_time_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case _:  
                print("Invalid choice! P.")


def main():

    employee = Employee("John boss")

    while True:
        print("""
        Menu:
        1. Check Employee Attendance
        2. Calculate Full-Time Employee Wage
        3. Calculate Part-Time Employee Wage
        """)
        
        choice = input("Enter your choice (1-3): ")

        if choice.isdigit():
            choice = int(choice)
            employee.process_choice(choice)
        else:
            print("Invalid input. Please enter a valid number.")
            continue

if __name__ == '__main__':
    main()
