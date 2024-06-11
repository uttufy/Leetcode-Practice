class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = defaultdict(int)
        res = 0

        for c in s:
            count[c] += 1
            if count[c] % 2 == 0:
                res += 2

        
        for c in count.values(): 
            if c % 2 != 0: 
                res+=1 
                break

        return res

        