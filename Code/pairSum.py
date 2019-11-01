"""
Given 2 lists find pair(s) of numbers from list1 and list2 which add up closest
to a target t.
For eg. l1 = [1,4,7,3] l2 = [2,0,4,8] and t = 11 should return the pairs (7,4),
(3,8) and (4,8) because their sums are 11 or closest to 11.
"""
class Solution:
  """
  to solve this problem consider a matrix of all elements from both lists in
  sorted order.
  Start with the last element on 1st row, this is the sum of l1[0] and l2[len(l2)-1]
  if this sum is less than t - 1 then all elements to the left of this cell are
  less than t - 1 and do not need to be processed. move to the cell below this by incrementing
  i by 1 but keeping j the same. If the sum is greater than t + 1 then all cells below this
  are greater than t + 1 and need not be processed. Move to the left of this cell by
  decrementing j by 1 and keeping i the same. If the sum is t or t - 1, note down the pairs
  and the sum and move to the left of cell as above, if the sum is t + 1, note down the pairs
  and move to cell below this one.
  You should have a list of all pairs that add up to t - 1, t or t + 1. Any of these can be the
  answer.
  """
  sum_pair_dict = {}

  def sum_pair(self, l1, l2, t):
    i, j = 0, len(l2) - 1
    sum = 0
    while i != len(l1) and j >=0:
      sum = l1[i] + l2[j]
      if sum > t + 1:
        j -= 1
        continue
      if sum < t - 1:
        i += 1
        continue
      if sum not in self.sum_pair_dict:
        self.sum_pair_dict[sum] = [(l1[i], l2[j])]
      else:
        self.sum_pair_dict[sum].append((l1[i], l2[j]))
      if sum <= t:
        i += 1
      else:
        j -= 1

l1, l2 = [1,4,7,3], [2,0,4,8]
t = 11

s = Solution()
s.sum_pair(sorted(l1), sorted(l2), t)
print(repr(s.sum_pair_dict)) # {11: [(3, 8), (7, 4)], 12: [(4, 8)]}
