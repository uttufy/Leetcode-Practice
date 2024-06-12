class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        
        a = 0
        b = x

        while x:
            l = x % 10
            a = a * 10
            a = a + l
            x = x // 10
        
        return a == b