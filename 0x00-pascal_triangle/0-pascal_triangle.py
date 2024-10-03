def pascal_triangle(n):
    # If n is less than or equal to 0, return an empty list
    if n <= 0:
        return []
    
    # Initialize the triangle with the first row
    triangle = [[1]]
    
    # Generate the rows of Pascal's Triangle
    for i in range(1, n):
        # Start the row with 1
        row = [1]
        # Fill in the middle elements
        for j in range(1, i):
            # Each element is the sum of the two elements above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End the row with 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)
    
    return triangle
