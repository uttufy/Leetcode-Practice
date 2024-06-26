class MyQueue(object):

    def __init__(self):
        self.stack = []
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.stack.append(x)
        

    def pop(self):
        """
        :rtype: int
        """
        # HACKY in STACK we cannot shift element using i+1 index
        remove = self.stack[0]
        for i in range(len(self.stack)):
            if i == len(self.stack) - 1:
                self.stack.pop()
            else:
                self.stack[i] = self.stack[i+1]
        return remove

        

    def peek(self):
        """
        :rtype: int
        """
        return self.stack[0]
        
        

    def empty(self):
        """
        :rtype: bool
        """
        return len(self.stack) == 0

        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()