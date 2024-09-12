
import random

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

    def process_choice(self, choice,company_name, wage_per_hour, full_day_hours, part_time_hours, working_days, max_working_hours, max_working_days):
        match choice:
            case 1:
                print(f"{self.name} is {'Present' if self.attendance_check() == 1 else 'Absent'}.")
            case 2:
                if self.attendance_check() == 1:
                    full_day_wage = self.calculate_full_day_wage(wage_per_hour, full_day_hours)
                    print(f"{self.name} is Present. Full-time wage: {full_day_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 3:
                if self.attendance_check() == 1:
                    part_time_wage = self.calculate_part_time_wage(wage_per_hour, part_time_hours)
                    print(f"{self.name} is Present. Part-time wage: {part_time_wage} rupees.")
                else:
                    print(f"{self.name} is Absent. No wage today.")
            case 4:
                is_part_time = input("Is this a part-time employee? (y/n): ").lower() == 'y'
                total_wage = self.calculate_monthly_wage(wage_per_hour, full_day_hours, part_time_hours, working_days, is_part_time)
                print(f"\nTotal wage for the month: {total_wage} rupees.")
            case 5:
                is_part_time = input("Is this a part-time employee? (y/n): ").lower() == 'y'
                total_wage = self.calculate_wages_for_month_until(wage_per_hour, full_day_hours, part_time_hours, max_working_hours, max_working_days, is_part_time)
                print(f"\nTotal wage for the month until limit is: {total_wage} rupees.")
            case _:
                print("Invalid choice! Please select a valid option.")

def main():

    # Collect company-specific details
    
    A_company_name = 'microsoft'
    A_wage_per_hour = 20
    A_full_day_hours = 8
    A_part_time_hours = 4
    A_working_days = 20
    A_max_working_hours = 100
    A_max_working_days = 20
    employee1 = Employee("charan") 
    

    B_company_name = 'google'
    B_wage_per_hour = 30
    B_full_day_hours = 8
    B_part_time_hours = 4
    B_working_days = 22
    B_max_working_hours = 100
    B_max_working_days = 20
    employee2 = Employee("ram") 
    



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
            company_name = input("enter company name: ").strip()
            if company_name.lower() == "microsoft":
                employee1.process_choice(choice,A_company_name,A_wage_per_hour,A_full_day_hours,A_part_time_hours,A_working_days,A_max_working_hours,A_max_working_days)
            elif company_name.lower() == "google": 
                employee2.process_choice(choice,B_company_name,B_wage_per_hour,B_full_day_hours,B_part_time_hours,B_working_days,B_max_working_hours,B_max_working_days) 
            else:
                print("invalid")

        else:
            print("Invalid input. Please enter a valid number.")

if __name__ == '__main__':
    main()

