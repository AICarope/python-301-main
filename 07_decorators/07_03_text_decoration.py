# Write a decorator that literally decorates text output.
# Make it so the symbol it uses can be an argument to the decorator
#
# The output of a function that returns `"Hello"` that has been
# decorated like with `@decorate("*")` should look like this:
#
# ******************************
# Hello
# ******************************


# Define the decorator with a parameter for the decoration symbol
def decorate(symbol):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the original function
            result = func(*args, **kwargs)
            # Create a line of symbols with the same length as the result
            decoration_line = symbol * (len(result) + 4)  # +4 for padding
            # Return the decorated text
            decorated_text = f"{decoration_line}\n* {result} *\n{decoration_line}"
            return decorated_text
        return wrapper
    return decorator

# Use the decorator on a function with the specified symbol
@decorate("*❤*")
def say_hello():
    return "Hello", "world" , "and beyond"
# Example usage
print(say_hello())