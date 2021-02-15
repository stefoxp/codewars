"""
Description

Write a function that accepts the current position of a knight in a chess board, it returns the possible positions that it will end up after 1 move. The resulted should be sorted.
Example

"a1" -> ["b3", "c2"]
"""


def possible_positions(pos):
    columns = ("a", "b", "c", "d", "e", "f", "g", "h")
    rows = ("1", "2", "3", "4", "5", "6", "7", "8")
    combo = ((-1, -2), (-1, 2), (1, -2), (1, 2), 
             (-2, -1), (2, -1), (-2, 1), (2, 1))
             
    positions = []
             
    col_ind = columns.index(pos[0])
    row_ind = rows.index(pos[1])
            
    for c in combo:
        col = col_ind + c[0]
        row = row_ind + c[1]
        
        if (0 <= col < 8) and (0 <= row < 8):
            positions.append(columns[col] + rows[row])
            
        positions.sort()
    
    return positions
