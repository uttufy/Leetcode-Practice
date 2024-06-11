class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        
        temp = list(magazine)

        for i in range(len(ransomNote)):
            if ransomNote[i] not in temp:
                return False
            temp.remove(ransomNote[i])

        return True
        