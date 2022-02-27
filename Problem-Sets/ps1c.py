"""
Part C: Finding the right amount to save
How much should you save each month to achieve this?
In this problem, you are going to write a program to answer that question.

To simplify things, assume:
- Your semiannual raise is .07 (7%)
- Your investments have an annual return of 0.04 (4%)
- The down payment is 0.25 (25%) of the cost of the house
- The cost of the house that you are saving for is  $1𝑀.
- You are now going to try to find the best rate of savings to achieve a down payment on a  $1𝑀  house in 36 months.

Since hitting this exactly is a challenge, we simply want your savings to be within  $100  of the required down payment.
"""


def savings_rate(base_annual_salary):
    # Fixed variables
    total_cost = 1000000  # $1M total cost of the house
    semi_annual_raise = 0.07  # 7% raise every 6 months
    monthly_r = 0.04 / 12  # Monthly interest
    down_payment = 0.25 * total_cost  # 25% of the total cost
    monthly_salary = base_annual_salary / 12  # Annual salary divided by 12
    months = 36  # 36 months to achieve the down payment
    epsilon = 100  # Within $100 of the required down payment
    portion_saved = 10000  # 10000 for 100%

    # Dynamic variables
    current_savings = 0  # Starting with zero savings
    low, high = 0, portion_saved  # Binary Search variables
    steps = 0  # Steps taken during Binary Search

    while abs(down_payment - current_savings) > epsilon:
        steps += 1

        # All variables are reset to initial values for each iteration in the loop
        current_savings = 0
        annual_salary = base_annual_salary
        monthly_salary = annual_salary / 12
        # monthly_deposit = monthly_salary * (portion_saved * initial_high)

        for m in range(months):
            current_savings += (monthly_salary * (portion_saved/10000)) + (current_savings * monthly_r)
            if m % 6 == 0 and m > 0:
                monthly_salary += monthly_salary * semi_annual_raise

        initial_portion_saved = portion_saved
        if current_savings < down_payment:
            low = portion_saved
        else:
            high = portion_saved

        portion_saved = (low + high) // 2

        if initial_portion_saved == portion_saved:
            break

    return portion_saved/10000, steps


def main():
    test_cases = [150000, 300000, 10000]

    for salary in test_cases:
        savings_perc, steps = savings_rate(salary)
        print(f'Enter the starting salary: {salary}')

        if int(savings_perc) == 1:  #
            print('It is not possible to save for a down payment in 36 months with this salary.')
        else:
            print(f'Best savings rate: {savings_perc}')
            print(f'Steps in bisection search: {steps}\n')


if __name__ == '__main__':
    main()
