class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        if len(nums) == 1:
            return nums[0]


        n = len(nums)//2
        count = {}
        for i in nums:
            if i in count:
                if count[i] == n:
                    return i
                count[i] = count.get(i,0) + 1
            else:
                count[i] = 1
                    
        return 

                