def pascal_triangle(n):
    """
    Returns a list of lists of integers representing Pascal's triangle of n.
    """
    if n <= 0:
        return []

    # Initialize Pascal's triangle with the first row
    triangle = [[1]]

    # Generate each row
    for i in range(1, n):
        prev_row = triangle[i - 1]
        # Start the row with 1
        row = [1]
        
        # Each value in the middle of the row is the sum of two values above it
        for j in range(1, i):
            row.append(prev_row[j - 1] + prev_row[j])
        
        # End the row with 1
        row.append(1)
        triangle.append(row)

    return triangle
