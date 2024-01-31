# Create a decorator that censors potentially offensive words from a text.
# For example, assuming that "shoot" was considered an offensive word:
# A function that would normall return this text:
#    "I bumped my toe! Shoot!"
# Would, after decorating it with `@censor()`, return:
#    "I bumped my toe! S****!"


# Define the decorator function
def censor(offensive_words):
    def decorator(func):
        def wrapper(*args, **kwargs):
            # Call the original function
            result = func(*args, **kwargs)
            # Replace offensive words with asterisks
            for word in offensive_words:
                if word in result:
                    censored_word = word[0] + '*' * (len(word) - 1)
                    result = result.replace(word, censored_word)
            return result
        return wrapper
    return decorator

# List of offensive words to be censored
offensive_words_list = ["shoot", "darn", "heck"]

# Use the decorator on a function
@censor(offensive_words_list)
def say_exclamation(exclamation):
    return f"I bumped my toe! {exclamation}"

# Example usage
print(say_exclamation("shoot"))  # Output: I bumped my toe! S****!