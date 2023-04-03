def largest_product(series, size):
    # If the size is negative, raise an error
    if size < 0:
        raise ValueError("span must not be negative")
        
    # If the series is empty and the size is positive, raise an error
    if series == "" and size > 0:
        raise ValueError("span must be smaller than string length")

    # If the series is not empty but cannot be converted to an integer, raise an
    # error
    try:
        series != "" and int(series)
    except ValueError:
        raise ValueError("digits input must only contain digits")

    # If the size is bigger than the series, raise an error
    if size > len(series):
        raise ValueError("span must be smaller than string length")

    # Special case: If the series is empty and the size is zero, the largest
    # product is 1
    if series == "" and size == 0:
        return 1

    # Before any series are calculated, 0 is the largest product
    largest_product = 0

    # Loop through a range starting at 0 and ending at the end of the series,
    # minus the size
    for i in range(len(series) - size + 1):
        # Get a slice of the series that starts at the current position and is
        # the length of the given size
        subseries = series[i:i + size]

        # The product starts at 1
        product = 1

        # For each digit in the slice...
        for digit in subseries:

            # Multiply the current product by the digit
            product *= int(digit)

        # If the calculation resulted in a product larger than the current
        # largest, set the new product as the largest
        if product > largest_product:
            largest_product = product

    # Return the largest product
    return largest_product
