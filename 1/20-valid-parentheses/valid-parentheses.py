class Solution(object):
    
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        map = {')' : '(', ']' : '[', '}': '{'}
        brackets = ['(', '[', '{']

        stack = []


        for c in s:
            if c in brackets:
                stack.append(c)
            elif c in map:
                if not stack:
                    return False
                elif map[c] == stack[-1]:
                    stack.pop()
                else:
                    return False
        
        return len(stack) == 0
