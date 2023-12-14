class Solution:
    def climbStairs(self, n: int) -> int:
        head, tail = 1, 1

        for i in range(n -1):
            temp = head
            head = head + tail
            tail = temp

        return head