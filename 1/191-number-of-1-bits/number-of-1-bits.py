class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """

        ## More optimised

        count = 0 
        while n>0:
            count += n%2
            n //=2
        
        return count



        ## Brute force 
        
        # def convert_dec_to_bin(self, n):
        #     bin = ""
        #     while n>0:
        #         rem = n % 2
        #         bin = bin + str(rem)
        #         n //= 2

        #     return bin[::-1]
        

        # res = convert_dec_to_bin(self,n)
        # count = 0

        # for c in res:
        #     if c == '1': count+=1

        # return count


        