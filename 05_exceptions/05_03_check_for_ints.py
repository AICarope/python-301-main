# Create a script that asks a user to input an integer, checks for the
# validity of the input type, and displays a message depending on whether
# the input was an integer or not.
# The script should keep prompting the user until they enter an integer.

while True:
    # Ask the user to input an integer
    user_input = input("Please enter an integer: ")

    try:
        # Try to convert the input to an integer
        user_number = int(user_input)
        # If the conversion is successful, print a message and break out of the loop
        print("Thank you! You have entered an integer: {}".format(user_number))
        break
    except ValueError:
        # If a ValueError occurs (i.e., the input is not an integer), prompt the user again
        print("That's not an integer. Please try again.")