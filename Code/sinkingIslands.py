"""
Given a matrix, find the number of islands. An island is defined as a 1 or a
group of 1s surrounded by 0
eg - [[1,1,0,0],[1,0,0,0],[1,0,1,0],[0,0,0,0]] should return 2.
There is a 1 at position (2,2) that is surrounded by 0s and
there is a group of adjacent 1s at positions (0,0), (0,1),(1,0) and (2,0)
that are surrounded by 0s. Note that the second group will count as 1 island
and not 4 different islands.
"""
def get_island_count(list):
    """
    To solve this use a sinking island approach. Iterate over the matrix.
    If a 1 is encountered then increment count after sinking all adjacent 1s.
    By sinking all adjacent 1s we are making sure that all of these count as
    1 island.
    """
  count = 0
  if len(list) == 0:
    print("0 islands as matrix is empty")
    return 0
  for i in range(len(list)):
    for j in range(len(list[0])):
      if list[i][j]:
        count += sink_adjacent_ones(list,i,j)
        print("count is {} when i={} and j={}".format(count,i,j))
  print("final count:",count)
  return count

def sink_adjacent_ones(array, x, y):
  if x < 0 or x >= len(array) or y < 0 or y >= len(array[x]) or array[x][y] == 0:
    return 0
  array[x][y] = 0
  sink_adjacent_ones(array,x-1,y)
  sink_adjacent_ones(array,x+1,y)
  sink_adjacent_ones(array,x,y-1)
  sink_adjacent_ones(array,x,y+1)
  return 1

l = [[1,1,0,0],[1,0,0,0],[1,0,1,0],[0,0,0,0]]
get_island_count(l)
