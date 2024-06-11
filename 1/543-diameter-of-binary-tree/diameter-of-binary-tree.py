# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int

        """

        global res
        res = 0
        def dfs(root,h):
            global res # nonlocal in python3
            if not root: return 0

            left = dfs(root.left, h) 
            right = dfs(root.right, h)

            res = max(res, left+right)
            return max(left, right) + 1
        

        dfs(root, 0)
        return res
        