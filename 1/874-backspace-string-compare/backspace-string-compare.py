class Solution(object):
    def backspaceCompare(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        s = s[::-1]
        t = t[::-1]

        s1 = ""
        t1 = ""
        x = 0
        y = 0

        for i in range(len(s)):
            if s[i]=='#':
                x+=1
            elif x==0:
                s1+=s[i]
            else:
                x-=1


        for i in range(len(t)):
            if t[i]=='#':
                y+=1
            elif y==0:
                t1+=t[i]
            else:
                y-=1
                

        if len(s1) != len(t1): return False

        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return False

        return True
                
        