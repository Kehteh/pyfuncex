# from functions_challenges import
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

# My version:

# def relay_total_distance_kms(prompt_distance: str, prompt_runners: str, distance_in_miles: float):
    
#     user_input1 = input(f"{prompt_distance}")
#     user_input_float1 = float(user_input1)
    

#     user_input2 = input(f"{prompt_runners}")
#     user_input_float2 = float(user_input2)

#     distance_in_miles = user_input_float1 * user_input_float2

#     return print(distance_in_miles * 1.60934)

# relay_total_distance_kms("Please enter a distance: "f"{prompt_distance}")
# relay_total_distance_kms("Please enter number of runners: "f"{prompt_runners}")

# chatGPT's version:

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


   