class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Complexity O(N)
        if len(s)<2:
            return len(s)

        res = 0

        head = 1
        tail = 0 
        curr = ""

    
        while head<len(s):
            if s[head]!=s[tail] and s[head]!=s[head-1] and not s[head] in curr:
                head+=1
            else:
                res = max(head-tail,res)
                while s[tail]!=s[head] and tail<head: tail+=1
                tail+=1
                head+=1
            curr=s[tail:head]

        return max(res,len(curr))
        