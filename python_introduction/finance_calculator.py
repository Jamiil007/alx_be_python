#Asking user about their monthly income
monthly_income = float(input("Enter your monthly income: "))

#Asking user about their monthly expenses
monthly_expenses = float(input("Enter your monthly expenses: "))

#Calculating monthly savings
monthly_savings = monthly_income - monthly_expenses

#Printing the result
projected_savings = monthly_savings * 12 + (monthly_savings * 12 * 0.05)

#Displaying the user's monthly savings
print(f"Your monthly savings are ${monthly_savings:.2f}.")

#Displaying the projected savings after one year
print(f"Projected savings after one year, with interest, is: ${projected_savings:.2f}.")
