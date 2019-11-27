"""
eg - 'bbbab' output = 4 as 'bbbb' is the longest palindromic subsequence
Logic - Use dp starting from the last character
at every step check if the string from this character to the end of string is a palindrome or not.
eg progression of dp array -
[0,0,0,0,1] only palindrome in 'b' is 'b'
[0,0,0,1,1] palindrome in 'ab' is 'b' or 'a'
[0,0,1,1,3] palindromes in 'bab' are 'b', 'a' or 'bab'
[0,1,2,2,3] palindromes in 'bbab' are 'b', 'bb', 'a', 'bbb' or 'bab'
[1,2,3,3,4] palindromes in 'bbbab' are 'b', 'bb', 'bbb', 'bab', 'bbbb'
"""

def longestPalindromeSubseq(self, s):
        if s == s[::-1]:
            return len(s)

        n = len(s)
        dp = [0 for j in xrange(n)]
        dp[n-1] = 1

        for i in xrange(n-1, -1, -1):   # can actually start with n-2...
            newdp = dp[:]
            newdp[i] = 1
            for j in xrange(i+1, n):
                if s[i] == s[j]:
                    newdp[j] = 2 + dp[j-1]
                else:
                    newdp[j] = max(dp[j], newdp[j-1])
            dp = newdp

        return dp[n-1]
