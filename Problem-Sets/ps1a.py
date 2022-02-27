"""
Problem Set 1
Part A: House Hunting
Write a program to calculate how many months it will take you to save up enough money for a down payment.

You will want your main variables to be floats, so you should cast user inputs to float.

Your program should ask the user to enter the following variables:
1. The starting annual salary (annual_salary)
2. The portion of salary to be saved (portion_saved)
3. The cost of your dream home (total_cost)
"""


def house_hunting(annual_salary, portion_saved, total_cost):
    # Fixed variables
    portion_down_payment = 0.25
    current_savings = 0
    r = 0.04
    monthly_salary = annual_salary / 12
    num_months = 0

    while current_savings < portion_down_payment * total_cost:
        current_savings += (monthly_salary * portion_saved) + current_savings * (r / 12)
        num_months += 1

    # Number of months
    return num_months


def main():
    test_cases = [
        (120000, 0.1, 1000000),
        (80000, 0.15, 500000)
    ]
    for annual_salary, portion_saved, total_cost in test_cases:
        num_months = house_hunting(annual_salary, portion_saved, total_cost)
        print(f'Enter your annual salary: {annual_salary}')
        print(f'Enter the percent of your salary to save, as a decimal: {portion_saved}')
        print(f'Enter the cost of your dream home: {total_cost}')
        print(f'Number of months: {num_months}\n')


if __name__ == '__main__':
    main()
