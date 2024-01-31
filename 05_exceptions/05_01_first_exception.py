# Write a script that generates an exception.
# Handle this exception with a try/except block.
# For example:
#
# list_ = ["hello world!"]
# print(list_[1])
#
# This raises and exception that needs to be handled.

list = ["hello world!"]
# print(list_[1])

try:
    print(list[2])
except IndexError as e:
    print("For your information an error index issue has occurred: ", e)


