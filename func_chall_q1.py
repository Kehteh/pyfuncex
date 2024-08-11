# Challenge 1 -> A Function to get a float from the user

def get_float(prompt_string: str):
    """A function that gets a float from the user and returns it.

    Arguments:
        - prompt_string: A string that will be shown to the user when they are 
            prompted to input the number.

    Returns:
        - A float converted from the user's input
    """
    user_input = input(prompt_string)

    try:
        user_input_float = float(user_input)
        return print(user_input_float)
    except ValueError:
        print("Enter a number only. Try again. ")


get_float("Please enter a number: ")