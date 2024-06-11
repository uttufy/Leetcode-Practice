class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        # fibonacci sequence

        # not neccessary
        # if n < 3:
        #     return n

        first = 1
        second = 1
        for i in range(1, n):
            temp = first 
            first = first + second
            second = temp
        
        return first
        