class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        res = strs[0]

        for s in strs[1:]:
            while s.find(res)!=0:
                res = res[:-1]
                if not res:
                    return ""
        return res
                
            

        