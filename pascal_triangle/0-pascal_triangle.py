def pascal_triangle(n):
    """
    Returns a list of lists representing the Pascal’s triangle of n rows
    """
    if n <= 0:
        return []

    # Initialize the Pascal's triangle with the first row
    triangle = [[1]]

    # Build each row from the second row to the nth row
    for i in range(1, n):
        # Start each row with a 1
        row = [1]
        # Fill in the middle values
        for j in range(1, i):
            # Each number is the sum of the two numbers directly above it
            row.append(triangle[i-1][j-1] + triangle[i-1][j])
        # End each row with a 1
        row.append(1)
        # Add the row to the triangle
        triangle.append(row)

    return triangle
