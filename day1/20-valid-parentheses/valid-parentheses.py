class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        map = {')' : '(', ']' : '[', '}': '{'}
        brackets = ['(', '[', '{']

        if len(s)%2!=0:
            return False

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




        