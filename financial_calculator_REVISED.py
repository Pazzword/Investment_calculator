import math

# Terminal clearing codes
# Great feature to use to clear you screen before displaying your code
CLEAR = "\033[2J"
CLEAR_AND_RETURN = "\033[H"

# Function to display instruction and obtain the answer from the user
def get_user_selection():
    # Loop to continuously ask the user until a valid selection is made
    while True:
        # Displaying a clear screen and instructions to the user
        selection = input(f'''{CLEAR}{CLEAR_AND_RETURN}
    <<<Thank you for choosing Anzor's financial calculator.>>>
                      
        For your convenience, we offer the following options:                  
1. Investment
    - Calculate the anticipated interest on your investment.
                      
2. Bond
    - Determine the repayment amount for a home loan.
                      

Please enter your choice as 'Investment' or 'Bond.'             
                      
If you would like to exit the program, type 'quit.' 
We appreciate your trust in our services. 
                      
TYPE OF INTEREST: ''').lower()
        # Check if the user's answer is a valid choice
        if selection in ["investment", "bond", "quit"]:
            if selection == "quit":
                print("Goodbye! Have a great day!")
            return selection
        else: 
            print("Invalid answer. Please enter 'Investment' or 'Bond'")

# Function to convert interest rate to a percentage
def convert_to_percentage(interest_rate):
    return interest_rate / 100

# Function to calculate investment interest
def calculate_investment_interest():
    # Get user inputs before calculation
    amount = float(input("Enter the amount that you are depositing: "))
    interest_rate = float(input("Enter the interest rate: "))
    number_of_years = int(input("How many years you wish to invest: "))
    user_interest = input("Would you like simple or compound interest: ")

    interest_rate = convert_to_percentage(interest_rate)

    # Calculate interest based on user choice
    if user_interest.lower() in ["simple", "simple interest"]:
        total_amount = amount * (1 + interest_rate * number_of_years)
        print(f"\nThe total amount after simple interest is: £{total_amount:.2f}\n")

    elif user_interest.lower() in ["compound", "compound interest"]:
        total_amount = amount * math.pow((1 + interest_rate), number_of_years)
        print(f"\nThe total amount after compound interest is: £{total_amount:.2f}\n")

# Function to calculate bond repayment
def calculate_bond_repayment():
    # Get user input for present value, annual interest rate, and number of months
    present_value = float(input("Enter the present value of the house: "))
    annual_interest_rate = float(input("Enter the annual interest rate: "))
    number_of_months = int(input("Enter the number of months over which the bond will be repaid: "))

    # Convert annual interest rate to monthly interest rate
    monthly_interest_rate = (annual_interest_rate / 100) / 12

    # Calculate bond repayment using the given formula
    repayment = (monthly_interest_rate * present_value) / (1 - math.pow((1 + monthly_interest_rate), -number_of_months))

    # Display the results
    print(f"\nThe total amount to repay each month will be:\t\t£{repayment:.2f}")
    print(f"The total amount to repay for {number_of_months} months will be:\t£{repayment * number_of_months:.2f}\n")

# Main function to execute the financial calculator
def main():
    selection = get_user_selection()
    
    if selection == "investment":
        calculate_investment_interest()
    elif selection == "bond":
        calculate_bond_repayment()

if __name__ == "__main__":
    main()