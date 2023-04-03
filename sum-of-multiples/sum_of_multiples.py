def sum_of_multiples(limit, factors):
    # Create an emply list that will be used to contain multiples
    multiples = []

    # For each factor given...
    for factor in factors:
        # If the factor is 0, go to the next factor
        if factor == 0:
            continue

        # Set/reset `multiples` to 0
        multiple = 0

        # While the current multiple is less than the given limit...
        while multiple < limit:
            # Append that multiple to the list of multiples
            multiples.append(multiple)

            # Increase the multiple by the current factor and then loop again
            multiple += factor
            
    
    # Remove duplicates by converting the list to a set and then back to a list
    unique_multiples = list(set(multiples))

    # Return the sum of the list of unique multiples
    return sum(unique_multiples)
