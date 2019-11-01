class Solution:
    # @param A : integer
    # @return a list of integers
    def allFactors(self, A):
        import math
        if A <= 0:
            return 0

        list1, list2 = [],[]
        for i in range(1, int(math.sqrt(A)) + 1):
            if i not in list1 and i not in list2 and A % i == 0:
                list1.append(i)
                list2.insert(0,A//i)
        list1.extend([x for x in list2 if x not in list1])
        return list1
