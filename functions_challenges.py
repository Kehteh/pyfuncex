#############################################################################################################
# Challenge 1 -> A Function to get a float from the user

# My version
# def get_float(prompt_string: str):
#     """A function that gets a float from the user and returns it.

#     Arguments:
#         - prompt_string: A string that will be shown to the user when they are 
#             prompted to input the number.

#     Returns:
#         - A float converted from the user's input
#     """
#     user_input = input(prompt_string)

#     try:
#         user_input_float = float(user_input)
#         return user_input_float
#     except ValueError:
#         print("Enter a number only. Try again. ")


# get_float("Please enter a number: ")

# chatGPTs version

def get_float(prompt_string: str):
    while True:
        user_input = input(prompt_string)
        try:
            user_input_float = float(user_input)
            return user_input_float
        except ValueError:
            print("Enter a number only. Try again.")

# Example of how to call the function
result = get_float("Please enter a number: ")
print(f"You entered: {result}")


#############################################################################################################
# Challenge 2 -> A Function to convert miles to km
# NOTE: 1 mile is 1.60934km

def miles_to_km(distance_in_miles: float):
    """A function to convert distance from miles to km

    Arguments: 
        - distance_in_miles: A float representing a distance in miles
    
    Returns
        - a float representing the distance in kilometers
    """
    
    return distance_in_miles * 1.60934

kilometers = miles_to_km(7)
print(kilometers)

#############################################################################################################
# Challenge 3 -> A function to calculate the total distance run in a relay

def relay_distance(distance_per_runner: float, number_of_runners: float):
    """A function to calculate the total distance run by a team of runners
    in a relay race.
    
    Arguments:
        - distance_per_runner: a float representing the amount each runner runs
            (in a relay race, all runners run the same distance!)
        - number_of_runners: a float representing the number of runners in a team
    
    Returns:
        - A float representing the total distance run.
    """
    
    return distance_per_runner * number_of_runners

distance_per_runner = 4.0  # Each runner covers 4 kilometers
number_of_runners = 5      # There are 5 runners in the relay

total_distance = relay_distance(distance_per_runner, number_of_runners)
print(f"The total distance of the relay race is {total_distance} kilometers.")

#############################################################################################################
# Challenge 4 (extra tricky, no tests for this one!)
# 
# See if you can write a single function that USES all three of the functions 
# you wrote for the above challenges.
#
# It should:
# - prompt the user for the distance each runner in the relay race will run (in miles)
# - prompt the user for the number of runners in a team
# - print the total distance run by the team, in kilometers!
# 
# No need for this function to accept any arguments or return any values.

def relay_total_distance_kms(prompt_distance: str, prompt_runners: str):
    # Getting user inputs
    user_input1 = input(prompt_distance)
    user_input_float1 = float(user_input1)

    user_input2 = input(prompt_runners)
    user_input_float2 = float(user_input2)

    # Calculating the total distance in miles
    distance_in_miles = user_input_float1 * user_input_float2

    # Converting the distance to kilometers and returning the value
    distance_in_kms = distance_in_miles * 1.60934
    print(f"Total distance in kilometers: {distance_in_kms:.2f}")

# Example of how to call the function
relay_total_distance_kms("Please enter the distance per runner in miles: ", "Please enter the number of runners: ")