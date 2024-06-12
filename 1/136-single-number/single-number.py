class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        for n in nums:
            res = res^n # XOR 

        return res 

#         Concept of XOR:
# XOR of zero and some bit returns that bit i.e. x^0 = x...
# XOR of two same bits returns 0 i.e. x^x = 0...
# And, x^y^x = (x^x)^y = 0^y = y...
# XOR all bits together to find the unique number.
        