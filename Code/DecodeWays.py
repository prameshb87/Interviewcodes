"""
Given a mapping from Alphabets to ints and a string representation of a number
return the number of ways this string can be decoded into character string.
eg. '12' may be decoded as 'AB' or 'L'

Approach - if a digit and its next digit total to something > 26 then there is
only 1 way this digit can be decoded. otherwise there are 2 ways, this digit or
this plus next digit to char.
for eg - '27345', there is only 1 way to decode the starting 2 as 27 is out of
bounds. So total num ways = num ways to decode '7345'. Same with the
starting 7 and so on. in total there is only 1 way to decode 27345
but for '26345', the first 2 can be decoded as 'B' but the 26 can also be decoded
as 'Z' so total num ways = num ways to decode '6345' plus num ways to decode
'345' so total 2 ways - 'AFCDE' or 'ZCDE' 
"""
class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        n = len(s)
        memo = [-1] * (n + 1)

        def numDecodingsHelper(s, k, memo):
            if k == 0:
                return 1
            idx = len(s) - k
            if s[idx] == '0':
                return 0
            if memo[k] != -1:
                return memo[k]
            result = numDecodingsHelper(s, k - 1, memo)
            if k >=2 and int(s[idx:idx + 2]) <= 26:
                result += numDecodingsHelper(s, k - 2, memo)
            memo[k] = result
            return result

        return numDecodingsHelper(s, n, memo)
