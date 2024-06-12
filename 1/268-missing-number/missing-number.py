class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()

        res = 0

        for n in nums:
            if res != n:
                return res
            res+=1
        
        return res