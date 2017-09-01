# data supplied by the user
annual_salary = float(input('Enter your annual salary: '))
portion_saved = float(input('Enter the percent of your salary to save, as a decimal: '))
total_cost = float(input('Enter the cost of your dream home: '))

# data that is fixed
portion_down_payment = 0.25
rate_of_return = 0.04
monthly_rate_of_return = rate_of_return / 12
monthly_salary = annual_salary / 12
down_payment = total_cost * portion_down_payment

# initially savings are zero. This variable is the core part of the decrementing
# function used to stop the algorithm
current_savings = 0.0

# this variable will hold the solution we seek after completion of the algorithm
months = 0