# Write a decorator function that wraps text output into quotes, e.g.:
# Hello world! ----> "Hello World!"
# You can use it to create quotes from text output.

def quote_decorator(func):
    def wrapper(*args, **kwargs):
        return '"' + func(*args, **kwargs) + '"'
    return wrapper

# Usage
@quote_decorator
def greet(name):
    return f"Hello, {name}!"


if __name__ == '__main__':
    print(greet("Carmen"))

 