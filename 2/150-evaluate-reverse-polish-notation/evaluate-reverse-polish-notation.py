class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        st = []
        op = ['+', '-', '*', '/']
        for n in tokens:
            if n not in op:
                st.append(int(n))
            else:
                a = st.pop()
                b = st.pop()
                
                if n=='+':
                    res = b + a
                elif n=='-':
                    res = b - a
                elif n=='*':
                    res = b * a
                elif n=='/':
                    if b*a >=0:
                        res = b // a
                    else:
                        res=-1*(abs(b)//abs(a))

            
                st.append(res)
        
        return st.pop()
        