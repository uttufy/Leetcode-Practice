class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # kadane ? 

        max_so_far = float('-inf')
        curr = 0
        for n in nums:
            curr = max(curr+n, n)
            max_so_far = max(max_so_far, curr)

        return max_so_far

        