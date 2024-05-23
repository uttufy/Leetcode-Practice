class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        # Brute force
        res = 0 
        i = 0

        expected = sorted(heights)
        while i<len(heights) :
            if heights[i] != expected[i]:
                res +=1
            i += 1 
        return res
        