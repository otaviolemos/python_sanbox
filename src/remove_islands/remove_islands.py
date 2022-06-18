def remove_islands(grid):
  ones_at_borders = find_ones_at_borders(grid)
  marked_matrix = traverse(grid, ones_at_borders)
  removed_islands = flip_ones_and_minus_ones(marked_matrix)
  return removed_islands

def flip_ones_and_minus_ones(grid):
  nrows = len(grid) 
  ncolumns = len(grid[0])
  for row in range(0, nrows):
    for column in range(0, ncolumns):
      if grid[row][column] == 1: grid[row][column] = 0
      if grid[row][column] == -1: grid[row][column] = 1
  return grid

def find_ones_at_borders(grid):
  ones_at_borders = list()
  nrows = len(grid) 
  ncolumns = len(grid[0])
  row = 0
  for column in range (0, ncolumns):
    if grid[row][column] == 1:
      ones_at_borders.append([row, column])
  row = nrows - 1
  for column in range (0, ncolumns):
    if grid[row][column] == 1:
      ones_at_borders.append([row, column])
  column = 0
  for row in range (0, nrows):
    if grid[row][column] == 1:
      ones_at_borders.append([row, column])
  column = ncolumns - 1
  for row in range (0, nrows):
    if grid[row][column] == 1:
      ones_at_borders.append([row, column])
  return set(tuple(i) for i in ones_at_borders)

def traverse(matrix, ones_at_borders):
  for one in ones_at_borders:
    traverse_and_tag(matrix, one)
  return matrix

def traverse_and_tag(matrix, cell): 
  row = cell[0]
  col = cell[1]
  matrix[row][col] = -1
  if (col-1 > 0 and matrix[row][col-1] and matrix[row][col-1] == 1):
    traverse_and_tag(matrix, [row, col-1])
  if (col+1 < len(matrix[row]) and matrix[row][col+1] and matrix[row][col+1] == 1):
    traverse_and_tag(matrix, [row, col+1])
  if (row-1 > 0 and matrix[row-1][col] and matrix[row-1][col] == 1):
    traverse_and_tag(matrix, [row-1, col])
  if (row+1 < len(matrix) and matrix[row+1][col] and matrix[row+1][col] == 1):
    traverse_and_tag(matrix, [row+1, col])