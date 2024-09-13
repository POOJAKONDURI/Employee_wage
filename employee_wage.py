from abc import ABC, abstractmethod
import random

# Interface for wage calculations
class IEmpWageBuilder(ABC):
    
    @abstractmethod
    def add_total_wage(self, wage):
        pass
    
    @abstractmethod
    def display_total_wage(self):
        pass
    
    @abstractmethod
    def process_choice(self, employee, choice):
        pass


class Employee:
    def __init__(self, name):
        self.name = name

    @classmethod
    def calculate_full_day_wage(cls, wage_per_hour, full_day_hours):
        return wage_per_hour * full_day_hours

    @classmethod
    def calculate_part_time_wage(cls, wage_per_hour, part_time_hours):
        return wage_per_hour * part_time_hours

    @staticmethod
    def attendance_check():
        return random.randint(0, 1)  # 1 means present, 0 means absent

    def calculate_monthly_wage(self, wage_per_hour, full_day_hours, part_time_hours, working_days, is_part_time=False):
        total_wage = 0
        for day in range(1, working_days + 1):
            attendance = self.attendance_check()
            if attendance == 1:
                if is_part_time:
                    daily_wage = self.calculate_part_time_wage(wage_per_hour, part_time_hours)
                    total_wage += daily_wage
                    print(f"Day {day}: {self.name} is Present (Part-Time). Wage: {daily_wage} rupees.")
                else:
                    daily_wage = self.calculate_full_day_wage(wage_per_hour, full_day_hours)
                    total_wage += daily_wage
                    print(f"Day {day}: {self.name} is Present (Full-Time). Wage: {daily_wage} rupees.")
            else:
                print(f"Day {day}: {self.name} is Absent. Wage: 0 rupees.")
        return total_wage

    def calculate_wages_for_month_until(self, wage_per_hour, full_day_hours, part_time_hours, max_working_hours, max_working_days, is_part_time=False):
        total_working_hours = 0
        total_working_days = 0
        total_wage = 0

        while total_working_hours < max_working_hours and total_working_days < max_working_days:
            attendance = self.attendance_check()
            if attendance == 1:
                if is_part_time:
                    daily_hours = part_time_hours
                    daily_wage = self.calculate_part_time_wage(wage_per_hour, part_time_hours)
                else:
                    daily_hours = full_day_hours
                    daily_wage = self.calculate_full_day_wage(wage_per_hour, full_day_hours)

                if total_working_hours + daily_hours > max_working_hours:
                    daily_hours = max_working_hours - total_working_hours
                    daily_wage = daily_hours * wage_per_hour

                total_working_hours += daily_hours
                total_wage += daily_wage
                total_working_days += 1

                print(f"Day {total_working_days}: {self.name} is Present. Wage: {daily_wage} rupees. Hours Worked: {daily_hours} hours.")
            else:
                total_working_days += 1
                print(f"Day {total_working_days}: {self.name} is Absent. Wage: 0 rupees. Hours Worked: 0 hours.")

        print(f"\nTotal working hours: {total_working_hours} hours.")
        print(f"Total working days: {total_working_days} days.")
        return total_wage


class EmpWageBuilder(IEmpWageBuilder):
    def __init__(self, company_name, wage_per_hour, full_day_hours, part_time_hours, working_days, max_working_hours, max_working_days):
        self.company_name = company_name
        self.wage_per_hour = wage_per_hour
        self.full_day_hours = full_day_hours
        self.part_time_hours = part_time_hours
        self.working_days = working_days
        self.max_working_hours = max_working_hours
        self.max_working_days = max_working_days
        self.total_wage = 0

    def add_total_wage(self, wage):
        self.total_wage += wage

    def display_total_wage(self):
        print(f"Total wage for {self.company_name}: {self.total_wage} rupees.")

    def process_choice(self, employee, choice):
        match choice:
            case 1:
                print(f"{employee.name} is {'Present' if employee.attendance_check() == 1 else 'Absent'}.")
            case 2:
                if employee.attendance_check() == 1:
                    full_day_wage = employee.calculate_full_day_wage(self.wage_per_hour, self.full_day_hours)
                    print(f"{employee.name} is Present. Full-time wage: {full_day_wage} rupees.")
                else:
                    print(f"{employee.name} is Absent. No wage today.")
            case 3:
                if employee.attendance_check() == 1:
                    part_time_wage = employee.calculate_part_time_wage(self.wage_per_hour, self.part_time_hours)
                    print(f"{employee.name} is Present. Part-time wage: {part_time_wage} rupees.")
                else:
                    print(f"{employee.name} is Absent. No wage today.")
            case 4:
                is_part_time = input("Is this a part-time employee? (y/n): ").lower() == 'y'
                total_wage = employee.calculate_monthly_wage(self.wage_per_hour, self.full_day_hours, self.part_time_hours, self.working_days, is_part_time)
                self.add_total_wage(total_wage)
                print(f"\nTotal wage for the month: {total_wage} rupees.")
            case 5:
                is_part_time = input("Is this a part-time employee? (y/n): ").lower() == 'y'
                total_wage = employee.calculate_wages_for_month_until(self.wage_per_hour, self.full_day_hours, self.part_time_hours, self.max_working_hours, self.max_working_days, is_part_time)
                self.add_total_wage(total_wage)
                print(f"\nTotal wage for the month until limit is: {total_wage} rupees.")
            case _:
                print("Invalid choice! Please select a valid option.")


def main():
    # Collect company-specific details and employee instances
    microsoft_builder = EmpWageBuilder('Microsoft', 20, 8, 4, 20, 100, 20)
    google_builder = EmpWageBuilder('Google', 30, 8, 4, 22, 100, 20)

    employee1 = Employee("Charan")
    employee2 = Employee("Ram")

    builders = {'microsoft': microsoft_builder, 'google': google_builder}

    while True:
        print("""
        Menu:
        1. Check Employee Attendance
        2. Calculate Full-Time Employee Wage
        3. Calculate Part-Time Employee Wage
        4. Calculate wages for a month
        5. Calculate Wages Until Total Hours or Days Reached
        """)
        
        choice = input("Enter your choice (1-5): ")
        if choice.isdigit():
            choice = int(choice)
            company_name = input("Enter company name (Microsoft/Google): ").strip().lower()

            if company_name in builders:
                builder = builders[company_name]
                employee = employee1 if company_name == 'microsoft' else employee2
                builder.process_choice(employee, choice)
                builder.display_total_wage()
                break
            else:
                print("Invalid company name.")
        else:
            print("Invalid input. Please enter a valid number.")
    

if __name__ == '__main__':
    main()
