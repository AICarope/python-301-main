# Read in the first number from `integers.txt`
# and perform a calculation with it.
# Make sure to catch at least two possible Exceptions (`IOError` and `ValueError`)
# with specific `except` statements, and continue to do the calculation
# only if neither of them applies.

file_name = 'integers.txt'



try:
    # Try opening the file to read
    with open(file_name, 'r') as file:
        # Read in the first line and assume it contains an integer
        first_number_str = file.readline()
        # Try converting the read string into an integer
        first_number = int(first_number_str)

except IOError:
    # Handle the IOError exception if the file can't be accessed
    print(f"Failed to open {file_name}. Please check if the file exists and you have read permissions.")

except ValueError:
    # Handle the ValueError if the conversion to integer fails
    print(f"The value read from {file_name} is not an integer.")

else:
    # Perform the calculation only if no exception was caught
    # Here we just do a simple operation, for example, multiplying by 2
    result = first_number * 2
    print(f"The result of the calculation is: {result}")