def transform(legacy_data):
    # Create an empty dictionary
    result = {}

    # Loop through all of the keys in `legacy_data`. Each key is a point value
    for points in legacy_data:
        # Each key (point value) corresponds to an array of letters. Loop
        # through the array of letters
        for letter in legacy_data[points]:
            # Assign the point value we're current in to the key
            # `letter.lower()` in our `result` dictionary. `.lower()` ensures
            # that all letters in the result are lowercase
            result[letter.lower()] = points

    # Return the dictionary filled with letters and corresponding point values
    return result;
