def calculate_bonus(years_of_service, salary):
    if years_of_service > 10:
        bonus_percentage = 0.10
    elif 6 <= years_of_service <= 10:
        bonus_percentage = 0.08
    else:
        bonus_percentage = 0.045
    
    return salary * bonus_percentage

years_of_service = float(input("Enter the years of service: "))
salary = float(input("Enter the salary: "))

bonus = calculate_bonus(years_of_service, salary)

print("Bonus Amount:",bonus)
