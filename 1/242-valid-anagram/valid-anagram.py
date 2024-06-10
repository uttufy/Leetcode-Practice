class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        if len(s) != len(t):
            return False
        
        count = {}

        for c in s:
            if c not in count:
                count[c] = 1
            else:
                count[c] = count[c] + 1
        
        for c in t:
            if c not in count:
                return False
            else:
                count[c] = count[c] - 1
        
        for i in count.keys():
            if count[i] != 0:
                return False
            
        return True


        