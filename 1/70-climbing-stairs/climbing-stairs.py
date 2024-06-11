class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fibonacci sequence

        first = 1
        second = 1
        for i in range(1, n):
            temp = first 
            first = first + second
            second = temp
        
        return first
        