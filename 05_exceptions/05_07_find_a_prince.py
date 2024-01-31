# Write a custom exception  that inherits from `Exception()`
# Open and read in the content of the book `.txt` files in the `books/` folder
# like you did in the previous exercise.
# Raise your `PrinceException()` if the first 100 characters of a book
# contain the string "Prince".

# Custom exception class definition
class PrinceException(Exception):
    """Exception raised when the string 'Prince' is found in the first 100 characters of a book."""
    pass

# Function to read the first 100 characters and check for the string "Prince"
def check_for_prince(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read(100)
            if "Prince" in content:
                raise PrinceException(f"The string 'Prince' was found in the first 100 characters of {file_path}")
    except FileNotFoundError as fnf_error:
        print(f"Error: {fnf_error}")
    except PrinceException as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Path to the 'books/' directory
directory = 'books/'

# Assuming you have a list of book filenames in the directory
book_filenames = ['book1.txt', 'book2.txt', 'book3.txt']  # Replace with actual filenames

# Loop through each book and check for the string "Prince"
for book_name in book_filenames:
    file_path = f"{directory}{book_name}"
    check_for_prince(file_path)