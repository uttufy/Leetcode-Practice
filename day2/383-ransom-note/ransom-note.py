class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        map = {}

        for i in magazine: 
            map[i] = map.get(i,0) + 1
        
        for i in ransomNote:
            if i not in map:
                return False
            elif map[i] == 0:
                return False
            else:
                map[i] = map[i] - 1
        
        return True

        