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


