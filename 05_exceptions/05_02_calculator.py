# Write a script that takes in two numbers from the user and calculates the quotient.
# Use a try/except statement so that your script can handle:
#
# - if the user enters a string instead of a number
# - if the user enters a zero as the divisor
#
# Test it and make sure it does not crash when you enter incorrect values.

def calculate_quotient(a, b):
    return a/b
 if __name__ =='__main__':
    while True:
        try:
            1 = float(input('enter the 1st number (dividend): ' ))
            2 = float(input('enter the 2nd number (divisor):'))

            result = calculate_quotient(1,2)
            print ('the quotient of {0} / {1} is: {2}'.format(1, 2, result))
            break
    except ValueError:
        print('enter valid number.')
    except ZeroDivisionError:
       print("The divisor cannot be zero. Please enter a non-zero number.")  