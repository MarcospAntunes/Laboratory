def search(matrix, target):
  rows = len(matrix)
  cols = len(matrix[0])
  
  row = 0
  col = cols - 1
  
  while row < rows and col >= 0:
    if matrix[row][col] == target:
      return "{},{}".format(row, col)
    elif matrix[row][col] > target:
      col -= 1
    else:
      row +=1
  
  return False


matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
target = 5
notInMatrix = 10

print(search(matrix, target))
print(search(matrix, notInMatrix))