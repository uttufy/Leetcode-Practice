# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        res = []
        queue = collections.deque()
        if root:
            queue.append(root)

        while queue:
            level = []
            n = len(queue)
            for i in range(n):
                node = queue.popleft()
                if node: 
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            if level:
                res.append(level)
        
        return res
