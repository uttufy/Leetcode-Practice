class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums = sorted(enumerate(nums), key=lambda a: a[1])

        left = 0 
        right = len(nums) - 1

        while left < right: 
            sum = nums[left][1] + nums[right][1]

            if sum == target:
                return [nums[left][0], nums[right][0]]
            if sum < target:
                 left += 1
            else:
                 right -= 1
        
        return []
        