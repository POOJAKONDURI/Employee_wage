import random

class Employee:
    def __init__(self, name, wage_per_hour=20, full_day_hours=8, part_time_hours=4, max_working_hours=100, max_working_days=20):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = full_day_hours
        self.part_time_hours = part_time_hours
        self.max_working_hours = max_working_hours
        self.max_working_days = max_working_days

    # UC1: Check if employee is present or absent
    def attendance_check(self):
        attendance = random.randint(0, 1)
        return attendance

    # UC2: Calculate Daily Wage (for full-time employees)
    def calculate_full_day_wage(self):
        return self.wage_per_hour * self.full_day_hours

    # UC3: Calculate Part-Time Wage
    def calculate_part_time_wage(self):
        return self.wage_per_hour * self.part_time_hours

    # UC6: Calculate wages until the total working hours or days condition is reached
    def calculate_wages_for_month(self, is_part_time=False):
        total_working_hours = 0
        total_working_days = 0
        total_wage = 0

        while total_working_hours < self.max_working_hours and total_working_days < self.max_working_days:
            attendance = self.attendance_check()
            if attendance == 1:
                total_working_days += 1
                if is_part_time:
                    daily_hours = self.part_time_hours
                    daily_wage = self.calculate_part_time_wage()
                else:
                    daily_hours = self.full_day_hours
                    daily_wage = self.calculate_full_day_wage()

                total_working_hours += daily_hours
                total_wage += daily_wage

                print(f"Day {total_working_days}: {self.name} is Present. Wage: {daily_wage} rupees. Hours Worked: {daily_hours} hours.")
            else:
                total_working_days += 1
                print(f"Day {total_working_days}: {self.name} is Absent. Wage: 0 rupees. Hours Worked: 0 hours.")

        print(f"\nTotal working hours: {total_working_hours} hours.")
        print(f"Total working days: {total_working_days} days.")
        return total_wage

    # UC4: Simulate switch-case using match statement
    def process_choice(self, choice):
        match choice:
            case 1:  
                print(f"{self.name} is {'Present' if self.attendance_check() == 1 else 'Absent'}.")
            case 2:  
                if self.attendance_check() == 1:
                    full_day_wage = self.calculate_full_day_wage()
                    print(f"{self.name} is Present. Full-time wage: {full_day_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 3:  
                if self.attendance_check() == 1:
                    part_time_wage = self.calculate_part_time_wage()
                    print(f"{self.name} is Present. Part-time wage: {part_time_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 4:  
                is_part_time = input("Is this a part-time employee? (y/n): ").lower() == 'y'
                total_wage = self.calculate_wages_for_month(is_part_time)
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
            employee.process_choice(choice)
        else:
            print("Invalid input. Please enter a valid number.")
            continue

if __name__ == '__main__':
    main()
