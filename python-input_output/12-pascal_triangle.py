from typing import List

def build_pascal_triangle(limit: int) -> List[List[int]]:
    """
    Constructs Pascal's triangle up to 'limit' rows.
    """
    if limit <= 0:
        return []

    # Initialize with the tip of the triangle
    rows = [[1]]

    while len(rows) < limit:
        last_row = rows[-1]
        next_row = [1] # Start with 1
        
        # Calculate the middle elements
        for i in range(len(last_row) - 1):
            current_sum = last_row[i] + last_row[i + 1]
            next_row.append(current_sum)
            
        next_row.append(1) # End with 1
        rows.append(next_row)

    return rows
