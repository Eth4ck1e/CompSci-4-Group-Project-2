def convert_months_to_years_months(total_months):
    """
    Converts a total number of months into a string representing the equivalent number of years and remaining months.

    Parameters:
        total_months (int): Total number of months to convert.

    Returns:
        str: A string representation of years and months.
    """
    years = total_months // 12  # Calculate full years
    months = total_months % 12  # Calculate remaining months
    return f"{years} years, {months} months"


def calculate_monthly_payment(principal, annual_interest, term_years):
    """
    Calculates the monthly payment required to repay a loan based on the principal, annual interest rate, and term.

    Parameters:
        principal (float): The loan amount.
        annual_interest (float): The annual interest rate as a percentage.
        term_years (int): The loan term in years.

    Returns:
        float: The calculated monthly payment amount.  This would be your mortgage payment.
    """
    monthly_interest_rate = annual_interest / 12 / 100  # Convert annual interest rate to a monthly decimal rate
    total_payments = term_years * 12  # Total number of monthly payments
    # Calculate the monthly payment using the formula for a fixed-rate mortgage
    monthly_payment = principal * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-total_payments)))
    return monthly_payment


def calculate_loan_repayment(principal, annual_interest_rate, extra_payment, monthly_payment, current_month=0,
                             total_interest_paid=0):
    """
    Recursively calculates the total interest paid and the time taken to repay the loan considering extra payments.

    Parameters:
        principal (float): The remaining principal of the loan.
        annual_interest_rate (float): The annual interest rate as a percentage.
        extra_payment (float): Additional payment made towards the principal.
        monthly_payment (float): The regular monthly payment amount calculated initially.
        current_month (int): Current month in the repayment schedule, default is 0.
        total_interest_paid (float): Cumulative interest paid till now, default is 0.

    Returns:
        tuple: Total interest paid and a string of the time taken in years and months.
    """
    # Base case: Check if the loan is fully repaid
    if principal <= 0:
        return total_interest_paid, convert_months_to_years_months(current_month)

    # Calculate interest for the current month
    monthly_interest_rate = annual_interest_rate / 12 / 100
    interest_payment = principal * monthly_interest_rate
    # Update total interest paid
    total_interest_paid += interest_payment
    # Calculate principal part of the payment
    principal_payment = monthly_payment - interest_payment
    # Subtract payments from principal
    principal -= (principal_payment + extra_payment)

    # Check if the principal is still above zero and recurse, else return final values
    if principal > 0:
        return calculate_loan_repayment(principal, annual_interest_rate, extra_payment, monthly_payment,
                                        current_month + 1, total_interest_paid)
    else:
        # Adjust the final month's principal payment if overpaid
        return total_interest_paid, convert_months_to_years_months(current_month)


# Default parameters
loan_amount = 1000000
annual_interest_rate = 7
loan_term = 30

# Calculate the standard monthly payment
monthly_payment = calculate_monthly_payment(loan_amount, annual_interest_rate, loan_term)

# Example 1: Standard repayment with no additional payments
extra_payment = 0
loan_repayment_info = calculate_loan_repayment(loan_amount, annual_interest_rate, extra_payment, monthly_payment)
print(f"Example 1 - Total Interest Paid: ${loan_repayment_info[0]:.2f}, Paid off in: {loan_repayment_info[1]}")

# Example 2: Additional payment equal to roughly 10% of the calculated monthly payment
extra_payment = monthly_payment * 0.10
loan_repayment_info = calculate_loan_repayment(loan_amount, annual_interest_rate, extra_payment, monthly_payment)
print(f"Example 2 - Total Interest Paid: ${loan_repayment_info[0]:.2f}, Paid off in: {loan_repayment_info[1]}")

# Example 3: Extra payment at 50% of the calculated monthly payment
extra_payment = monthly_payment * 0.50
loan_repayment_info = calculate_loan_repayment(loan_amount, annual_interest_rate, extra_payment, monthly_payment)
print(f"Example 3 - Total Interest Paid: ${loan_repayment_info[0]:.2f}, Paid off in: {loan_repayment_info[1]}")

# Example 4: 100% of the calculated monthly payment as the extra payment
extra_payment = monthly_payment
loan_repayment_info = calculate_loan_repayment(loan_amount, annual_interest_rate, extra_payment, monthly_payment)
print(f"Example 4 - Total Interest Paid: ${loan_repayment_info[0]:.2f}, Paid off in: {loan_repayment_info[1]}")
