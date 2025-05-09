__author__ = 'Chigozie Nnani, cfnnani@unc.edu, Onyen = cfnnani'

# Welcome users!
print("Welcome to the Compound Interest Calculator!")

# Ask user for original principal (P), interest rate (r), number of compoundings per year (n),  number of years to save (t)
original_principal = float(input("Please enter the initial amount of your investment: "))
interest_rate = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
years_to_save = int(input("Please enter the number of years for the investment: "))
compoundings_per_year = int(input("Please enter the number of compoundings per year: "))

# Display original principal (P), amount of interest earned (P'-P), total value at end of term (P')
interest_earned = original_principal * (1 + (interest_rate / compoundings_per_year)) ** (compoundings_per_year * years_to_save) - original_principal
total_value = original_principal + interest_earned

print(f"Original Investment: ${original_principal:,.2f}")
print(f"Interest Earned:     ${interest_earned:,.2f}")
print(f"Final Balance:       ${total_value:,.2f}\n")

# Ask user if they would like to compare to another savings option
compare_savings = input("Would you like to compare this to another savings option? (Y/N): ")
if compare_savings == "Y" or compare_savings == "y":
    original_principal1 = float(input("Please enter the initial amount of your investment: "))
    interest_rate1 = float(input("Please enter the interest rate (e.g., '.03' for 3% interest): "))
    years_to_save1 = int(input("Please enter the number of years for the investment: "))
    compoundings_per_year1 = int(input("Please enter the number of compoundings per year: "))

    interest_earned1 = original_principal1 * (1 + (interest_rate1 / compoundings_per_year1)) ** (compoundings_per_year1 * years_to_save1) - original_principal1
    total_value1 = original_principal1 + interest_earned1

    print(f"Original Investment: ${original_principal1:,.2f}")
    print(f"Interest Earned:     ${interest_earned1:,.2f}")
    print(f"Final Balance:       ${total_value1:,.2f}\n")

    if total_value1 > total_value:
        print("The second option will result in the largest final account balance.\n")
    elif total_value1 < total_value:
        print("The first option will result in the largest final account balance.\n")
    else:
        print("Both options will result in the same final account balance.\n")
        
else:
    exit()