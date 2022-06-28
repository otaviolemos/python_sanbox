def permutations(x, y, z, n):
  x_values = [x for x in range(0, x+1)]
  y_values = [y for y in range(0, y+1)]
  z_values = [z for z in range(0, z+1)]
  permutations = [[i, j, k] for i in x_values 
                 for j in y_values
                 for k in z_values 
                 if i+j+k != n]
  print(permutations)
  return permutations