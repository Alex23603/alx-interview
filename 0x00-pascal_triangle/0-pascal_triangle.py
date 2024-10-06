def pascal_triangle(n):
    if n <= 0:
        return []
    
    # Initialize the first row of Pascal's triangle
    triangle = [[1]]
    
    # Build the triangle row by row
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        
        # Calculate the in-between values as the sum of the two values above
        for j in range(1, i):
            row.append(triangle[i - 1][j - 1] + triangle[i - 1][j])
        
        # End each row with a 1
        row.append(1)
        triangle.append(row)
    
    return triangle
