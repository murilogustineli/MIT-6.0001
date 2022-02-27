"""
Problem Set 1
Part B: Saving, with a raise
Write a program to calculate how many months it will take you save up enough money for a down payment.
Like before, assume that your investments earn a return of r = 0.04 (or 4%)
and the required down payment percentage is 0.25 (or 25%).

Have the user enter the following variables:
1. The starting annual salary (annual_salary) 2
2. The percentage of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
4. The semiannual salary raise (semi_annual_raise)
"""


def saving_with_raise(annual_salary, portion_saved, total_cost, semi_annual_salary):
    # Fixed variables
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    num_months = 0

    while current_savings < portion_down_payment * total_cost:
        current_savings += (monthly_salary * portion_saved) + current_savings * (r / 12)
        if num_months % 6 == 0 and num_months != 0:
            monthly_salary += monthly_salary * semi_annual_salary
        num_months += 1

        # Number of months
    return num_months


def main():
    test_cases = [
        (120000, 0.05, 500000, 0.03),
        (80000, 0.1, 800000, 0.03),
        (75000, 0.05, 1500000, 0.05)
    ]
    for i, values in enumerate(test_cases):
        num_months = saving_with_raise(values[0], values[1], values[2], values[3])
        print(f'Test Case {i+1}:')
        print(f'Enter your annual salary: {values[0]}')
        print(f'Enter the percent of your salary to save, as a decimal: {values[1]}')
        print(f'Enter the cost of your dream home: {values[2]}')
        print(f'Enter the semiannual raise, as a decimal: {values[3]}')
        print(f'Number of months: {num_months}\n')


if __name__ == '__main__':
    main()
