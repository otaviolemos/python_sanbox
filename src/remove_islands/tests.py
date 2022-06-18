from remove_islands.remove_islands import find_ones_at_borders, remove_islands, traverse, traverse_and_tag

def test_remove_islands():
    assert remove_islands([
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 1, 0],
      [1, 1, 0, 0, 1, 0],
      [1, 0, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ]) == [
  [1, 0, 0, 0, 0, 0],
  [0, 0, 0, 1, 1, 1],
  [0, 0, 0, 0, 1, 0],
  [1, 1, 0, 0, 1, 0],
  [1, 0, 0, 0, 0, 0],
  [1, 0, 0, 0, 0, 1],
] 

def test_find_ones_at_borders():
  assert find_ones_at_borders([
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 1, 0],
      [1, 1, 0, 0, 1, 0],
      [1, 0, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ]) == {(0, 0), (5, 5), (3, 0), (1, 5), (5, 0), (4, 0)}

def test_traverse_and_tag():
  matrix = [
      [1, 0, 0, 0, 0, 0],
      [0, 1, 0, 1, 1, 1],
      [0, 0, 1, 0, 1, 0],
      [1, 1, 0, 0, 1, 0],
      [1, 0, 1, 1, 0, 0],
      [1, 0, 0, 0, 0, 1],
    ]
  ones_at_borders = find_ones_at_borders(matrix)
  changed_matrix = traverse(matrix, ones_at_borders)
  print(changed_matrix)
  assert changed_matrix == [
      [-1, 0, 0, 0, 0, 0],
      [0, 1, 0, -1, -1, -1],
      [0, 0, 1, 0, -1, 0],
      [-1, -1, 0, 0, -1, 0],
      [-1, 0, 1, 1, 0, 0],
      [-1, 0, 0, 0, 0, -1],
    ]