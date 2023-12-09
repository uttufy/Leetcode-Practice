class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if not len(s)==len(t):
            return False

        countS = {}
        countT = {}

        for c in s:
            countS[c] = countS.get(c, 0) + 1
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        for c in countS:
            if countS[c] != countT.get(c, 0):
                return False

        return True