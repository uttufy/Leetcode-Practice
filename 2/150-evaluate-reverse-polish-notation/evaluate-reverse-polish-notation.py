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

                        # in python
                        # 6//4 = 1
                        # -6//4 = -2
                        # to avoid this truncation we need to check sign
            
                st.append(res)
        
        return st.pop()
        