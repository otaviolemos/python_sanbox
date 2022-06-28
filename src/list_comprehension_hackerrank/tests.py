from permutations import permutations

def test_simple_input():
  x = 1
  y = 1
  z = 1
  n = 2
  assert permutations(x, y, z, n) == [[0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]