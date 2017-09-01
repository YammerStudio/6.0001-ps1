# data supplied by the user
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))

# data that is fixed
portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
total_cost = 1000000
down_payment = total_cost * portion_down_payment
monthly_deposit = monthly_salary * portion_saved
semi_annual_raise = 0.07
months = 36

# initially savings are zero. This variable is the core part of the decrementing
# function used to stop the algorithm
current_savings = 0.0

# use exhaustive enumeration to find the solution
while current_savings < down_payment:
    # problem states investment income and savings deposits occur at the end
    # of the month, so increment month before mutating current_savings
    months += 1
    current_savings *= 1 + monthly_rate_of_return
    current_savings += monthly_deposit
    # problem states that semi-annual raises take effect the next month, so 
    # mutate monthly_salary after mutating current_savings
    if months % 6 == 0:
        annual_salary *= 1 + semi_annual_raise
        monthly_salary = annual_salary / 12
        monthly_deposit = monthly_salary * portion_saved
    
print('Number of months:', months)