class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        ans=[0]
        for i in range(1, n+1):
            div = i//2
            if(i%2==1):
                ans.append(ans[div]+1)
            else:
                ans.append(ans[div])

        return ans


        