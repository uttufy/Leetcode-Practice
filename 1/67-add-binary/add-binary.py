class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        carry = 0
        res = ""

        a = a[::-1] # reverse the number
        b = b[::-1] # REverse

        for i in range(max(len(a), len(b))):
            x = int(a[i]) if i < len(a) else 0
            y = int(b[i]) if i < len(b) else 0

            total = x + y + carry
            char = total % 2
            res = str(char) + res
            carry = total // 2

        if carry: 
            res = "1" + res

        
        return res

                
