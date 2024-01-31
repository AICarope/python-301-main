# Create a custom decorator function that records the execution time of
# the decorated function and prints the time to your console when the function
# has finished execution.


import time

# Define the decorator function
def record_execution_time(func):
    def wrapper(*args, **kwargs):
        # Capture the start time
        start_time = time.time()
        
        # Call the original function
        result = func(*args, **kwargs)
        
        # Capture the end time
        end_time = time.time()
        
        # Calculate the execution time
        execution_time = end_time - start_time
        
        # Print the execution time
        print(f"{func.__name__} executed in {execution_time:.4f} seconds.")
        
        # Return the original function's result
        return result
    return wrapper

# Use the decorator on a function to record its execution time
@record_execution_time
def example_function():
    # An example function that sleeps for 1 second
    time.sleep(1)
    return "Function has finished execution."

# Example usage
example_function_result = example_function()
print(example_function_result)