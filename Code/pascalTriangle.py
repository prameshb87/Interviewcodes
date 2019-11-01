import copy
numRows = 5
output = []
for i in range(numRows):
  if i == 0:
    output.append([1])
    continue
  if i == 1:
    output.append([1,1])
    continue
  temp = copy.copy(output[i-1])
  length = len(output[i-1])
  for j in range(length):
    if j < length - 1:
      new_num = output[i-1][j+1] + output[i-1][j]
      print('new_num, j', new_num, j)
      temp.insert(j+1, new_num)
      print('j, temp', j, temp)
    # else:
    #   temp.insert(j+1, 1)
  output.append(temp)
  print('temp, i' ,temp, i)
  print('output, i', output, i)
