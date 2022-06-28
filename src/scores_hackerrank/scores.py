def scores():
  names = ["Rachel", "Mawer", "Sheen", "Shaheen"]
  scores = [-50, -50, -50, 51]
  students = []
  i = 0
  for name in names:
      students.append((name, scores[i]))
      i+=1
  students.sort(key=lambda item: item[1])
  worst_score = students[0][1]
  index_second_worst = 0
  while students[index_second_worst][1] == worst_score:
    index_second_worst += 1
  print(index_second_worst)
  second_lowest_score = students[index_second_worst][1]
  names_with_second_worst = []
  i = index_second_worst
  while i < len(students) and students[i][1] == second_lowest_score: 
      names_with_second_worst.append(students[i][0])
      i += 1
  names_with_second_worst.sort()
  for name in names_with_second_worst:
      print(name)

scores()