import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

import amortization as amort

# Import default loan values from amortization
loan_amount = amort.loan_amount
annual_interest_rate = amort.annual_interest_rate
loan_term = amort.loan_term
monthly_payment = amort.calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term)

# Range of extra payments from 0% to 200% of the monthly payment
extra_payment_percentages = list(range(0, 201, 10))
extra_payments = [monthly_payment * i * 0.01 for i in extra_payment_percentages]

# Lists to store results
interests_paid = []
times_to_payoff = []

# Collect data for each extra payment scenario
for extra_payment, percent in zip(extra_payments, extra_payment_percentages):
    loan_repayment_info = amort.calculate_loan_repayment(loan_amount, annual_interest_rate, extra_payment,
                                                         monthly_payment)
    interests_paid.append(loan_repayment_info[0])
    times_to_payoff.append(
        loan_repayment_info[1].split()[0])

# Convert times to integers for plotting
times_to_payoff = [int(time) for time in times_to_payoff]


# Function to format the tick marks as millions
def millions_formatter(x, pos):
    return f'${float(x / 1e6)}M'


# Plotting the results
plt.figure(figsize=(10, 5))
plt.subplot(1, 2, 1)
plt.plot(extra_payment_percentages, interests_paid, marker='o')
plt.title('Total Interest Paid vs. Extra Payment %')
plt.xlabel('Extra Payment %')
plt.ylabel('Total Interest Paid')
plt.gca().yaxis.set_major_formatter(mticker.FuncFormatter(millions_formatter))  # Apply formatting to y-axis
plt.grid(True)

plt.subplot(1, 2, 2)
plt.plot(extra_payment_percentages, times_to_payoff, marker='o', color='red')
plt.title('Years to Payoff vs. Extra Payment %')
plt.xlabel('Extra Payment %')
plt.ylabel('Years to Payoff')
plt.grid(True)

plt.tight_layout()

# Save the figure as a JPEG file
plt.savefig('loan_analysis_1.jpg')

plt.show()
