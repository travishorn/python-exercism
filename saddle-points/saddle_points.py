def saddle_points(matrix):
    # If the given matrix is empty, return an empty list
    if len(matrix) == 0:
        return [];

    # Use `*` to unpack the list of lists, then `zip` them together. This
    # transposes (or "rotates") the matrix. Now each "row" is a "column".
    cols = zip(*matrix)

    # Map over each row and get the largest number
    row_maxs = list(map(max, matrix))

    # Map over each col and get the smallest number
    col_mins = list(map(min, cols))

    # Create an empty list that we can append to
    saddle_points = []

    # Loop over each row
    for row_index, row in enumerate(matrix):
        # If the current row isn't the same length as the first row, the matrix
        # doesn't have an equal length in each row. It is irregular; raise an
        # exception.
        if len(row) != len(matrix[0]):
            raise ValueError("irregular matrix")
        
        # Loop over each number in the current row
        for col_index, n in enumerate(row):

            # If the current number is greater than or equal to the largest
            # number in the row AND it is less than or equal to the smallest
            # number in the column...
            if n >= row_maxs[row_index] and n <= col_mins[col_index]:
                # ...a saddle point was found. Append the row and column index
                # to the list
                saddle_points.append({ "row": row_index + 1, "column": col_index + 1})
    
    # Return the list of saddle points
    return saddle_points;
