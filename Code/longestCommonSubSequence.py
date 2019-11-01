"""
Given 2 strings s1 and s2, find the length of the longest common subsequence.
Eg s1 = 'abcbdf' s2 = 'acbcf'. The longest common subsequence is 'abcf' of
length 4.
"""
def lcs(s1, s2):
    """
    Consider a 2d matrix representing the lcs length between each string
    construction. For eg dp[1][1] represents length of lcs between strings
    'a' and 'a', dp[2][3] represents length of lcs between strings 'ab' and 'acb'
    Then dp[len(s1)+1][len(s2)+1] will represent the length of lcs between
    strings s1 and s2
    """
    m, n = len(s1), len(s2)
    dp = [[0 for _ in range(m+1)] for _ in range(n+1)]
    for i in range(1, m+1):
        for j in range(1, n+1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m+1][n+1]
 
