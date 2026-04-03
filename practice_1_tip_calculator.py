# Author: James Harris
# GitHub username: thestackman
# Date: 20260326
# Description:  Calculates a restaurant bill including tip and tax,
#               then prints an itemized summary.

# Get user input
subtotal = float(input("Enter the meal subtotal: "))
tip_rate = int(input("Enter tip percentage (e.g. 15 for 15%): "))
tax_rate = int(input("Enter your tax (e.g. 8 for 8%): "))

# Compute values
tip_amount = subtotal * tip_rate/100
tax_amount = subtotal * tax_rate/100
total_amount = subtotal + tip_amount + tax_amount

# Print user output
print("--- Bill Summary ---")
print(f"Subtotal: ${subtotal:,.2f}")
print(f"Tip Amount ({tip_rate}%): ${tip_amount:,.2f}")
print(f"Tax Amount ({tax_rate}%): ${tax_amount:,.2f}")
print(f"Total Amount: ${total_amount:,.2f}")