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




