grid = [
    [ 524, 523, 522, 521, 520, 519, 518, 517, 516 ],
    [ 546, 546, 531, 530, 529, 528, 527, 526, 525 ],
    [ 546, 546, 537, 536, 535, 534, 533, 532, 0 ]
    ]

mappings = {}

def make_grid_mappings():
    rownum = 0
    for row in grid:
        colnum = 0
        for col in row:
            mappings[grid[rownum][colnum]] = (rownum, colnum)
            colnum += 1
        rownum += 1
    
def gridno_to_coord(gridno):
    make_grid_mappings()
    return mappings[gridno]


# say lat varies from 36.6 to 36.8
# long from -121.0 to -121.8 (am I mixing e and w?)
def find_gridno(lat, long):
    gridheight = len(grid)
    gridwidth = len(grid[0])
    # etc. for now.  must sleep.

print gridno_to_coord(534)

(row, col) =  gridno_to_coord(534)

# 1 west, 1 north
print grid[row - 1][col - 1]
