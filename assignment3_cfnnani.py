__author__ = 'Chigozie Nnani, cfnnani@unc.edu, Onyen = cfnnani'

# Function that calculates the square root of a number using the Babylonian method
def babylonian_sqrt(n):
    epsilon = 0.0001
    estimate = n

    while True:
        previous_estimate = estimate
        estimate = (estimate + n / estimate) / 2

        if abs(estimate - previous_estimate) < epsilon:
            break
    return estimate

# Function that prompts the user to enter a positive integer value
def positive_int(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value > 0:
                return value
            else:
                print("Enter a positive integer value: ")
        except ValueError:
            print("Enter a positive integer value.")

# Function to handle square root calculation for a single value
def single_value_mode():
    n = positive_int("\nEnter a positive integer value: ")
    square_root = babylonian_sqrt(n)
    print(f"Value\tSquare Root")
    print(f"{n:>4}\t{square_root:>8.3f}")

# Function to handle square root calculation for a range of values
def range_mode():
    start = positive_int("\nEnter a positive integer value to start your range: ")

    while True:
        end = positive_int("Enter a positive integer value to end your range: ")
        if end >= start:
            break
        else:
            print("Please enter a value greater than or equal to the start value.")

    print(f"Value\tSquare Root")
    for i in range(start, end + 1):
        square_root = babylonian_sqrt(i)
        print(f"{i:>4}\t{square_root:>8.3f}")

# Main function for user input
def main():
    while True:
        mode = str(input("Enter 'single' or 'range' to solve for a single square root or a range of values, respectively: "))
        if mode == "single":
            single_value_mode()
            break
        elif mode == "range":
            range_mode()
            break
        else:
            print("Please enter 'single' or 'range'.")

# Ensure the main function runs when the script is executed
if __name__ == "__main__":
    main()