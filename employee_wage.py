import random

class Employee:
    def __init__(self, name, wage_per_hour=20, full_day_hours=8, part_time_hours=4, working_days=20):
        self.name = name
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = full_day_hours
        self.part_time_hours = part_time_hours
        self.working_days = working_days

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

    # UC5: Calculate wages for a month based on attendance and work type
    def calculate_monthly_wage(self, is_part_time=False):
        total_wage = 0
        for day in range(1, self.working_days + 1):
            attendance = self.attendance_check()
            if attendance == 1:
                if is_part_time:
                    daily_wage = self.calculate_part_time_wage()
                    total_wage += daily_wage
                    print(f"Day {day}: {self.name} is Present (Part-Time). Wage: {daily_wage} rupees.")
                else:
                    daily_wage = self.calculate_full_day_wage()
                    total_wage += daily_wage
                    print(f"Day {day}: {self.name} is Present (Full-Time). Wage: {daily_wage} rupees.")
            else:
                print(f"Day {day}: {self.name} is Absent. Wage: 0 rupees.")
        return total_wage

    # UC4: Simulate switch-case using match statement
    def process_choice(self, choice):
        match choice:
            case 1:  # Check Employee Attendance (UC1)
                print(f"{self.name} is {'Present' if self.attendance_check() == 1 else 'Absent'}.")
            case 2:  # Calculate Daily Wage (Full-Time) (UC2)
                if self.attendance_check() == 1:
                    full_day_wage = self.calculate_full_day_wage()
                    print(f"{self.name} is Present. Full-time wage: {full_day_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 3:  # Calculate Part-Time Wage (UC3)
                if self.attendance_check() == 1:
                    part_time_wage = self.calculate_part_time_wage()
                    print(f"{self.name} is Present. Part-time wage: {part_time_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 4:  # Calculate Monthly Wage (UC5)
                is_part_time = input("Is this a part-time employee? (y/n): ").lower() == 'y'
                total_wage = self.calculate_monthly_wage(is_part_time)
                print(f"Total wage for {self.working_days} days: {total_wage} rupees.")
            case _:
                print("Invalid choice! Please select a valid option.")


def main():
    employee = Employee("John Doe")  # Create an Employee object

    while True:
        print("""
        Menu:
        1. Check Employee Attendance
        2. Calculate Full-Time Employee Wage
        3. Calculate Part-Time Employee Wage
        4. Calculate Monthly Employee Wage
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

