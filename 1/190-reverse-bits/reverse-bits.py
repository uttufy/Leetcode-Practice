class Solution:
    def reverseBits(self, n: int) -> int:

        # Initialize the reversed number to 0
        reversed_num = 0
        
        # Iterate over all 32 bits of the given number
        for i in range(32):
            lsb = n & 1
            temp = lsb << (31-i)
            reversed_num = reversed_num | temp

            n = n >> 1
        return reversed_num