import numpy as np
import matplotlib.pyplot as plt
import amortization as amort

from amortization import calculate_monthly_payment, calculate_loan_repayment

# Import default loan values from amortization module
loan_amount = amort.loan_amount
annual_interest_rate = amort.annual_interest_rate
loan_term = amort.loan_term
monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term)

# Generate percentages from 0% to 200% of the monthly payment
percentage_extra_payments = np.linspace(0, 200, 50)  # 50 points from 0% to 200%
extra_payments = [monthly_payment * (p / 100) for p in percentage_extra_payments]  # Calculate actual payment amounts

interests_paid = []

# Collect total interest paid for each extra payment scenario
for extra_payment in extra_payments:
    total_interest, _ = calculate_loan_repayment(loan_amount, annual_interest_rate, extra_payment, monthly_payment)
    interests_paid.append(total_interest)

# Base interest paid (interest paid with 0% extra payment)
base_interest_paid = interests_paid[0]

# Convert total interest paid into a percentage of the base interest paid
interests_paid_percent = [(interest / base_interest_paid) * 100 for interest in interests_paid]

plt.figure(figsize=(8, 6))
plt.plot(percentage_extra_payments, interests_paid_percent, marker='o', label='Percentage of Interest Saved')
plt.xlabel('Extra Payment as % of Monthly Payment')
plt.ylabel('Interest Paid as % of Base Interest Paid')
plt.title('Interest Paid Relative to Base Case with No Extra Payments')
plt.gca().invert_yaxis()  # Invert y-axis to show decreasing percentages upwards

# y-ticks every 10%
plt.yticks(np.arange(0, 110, 10))

# x-ticks every 10%
plt.xticks(np.arange(0, 210, 10))

plt.grid(True)
plt.savefig('loan_analysis_2.jpg')
plt.show()
