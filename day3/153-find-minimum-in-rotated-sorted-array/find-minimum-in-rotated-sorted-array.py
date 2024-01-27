class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        res = nums[0]
        for i in nums:
            res = min(res, i)
        
        return res
        