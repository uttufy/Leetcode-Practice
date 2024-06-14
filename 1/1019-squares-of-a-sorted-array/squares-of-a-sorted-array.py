class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # for i in range(len(nums)):
        #     nums[i]*=nums[i]

        # return sorted(nums)

        # Two Pointers

        n = len(nums)
        s = 0
        e = n - 1
        ans = [0] * n
        for i in range(n-1, -1, -1):
            if abs(nums[s])>abs(nums[e]):
                ans[i] = nums[s]**2 # square basically
                s = s + 1
            else:
                ans[i] = nums[e]**2 # square basically
                e = e - 1

        return ans