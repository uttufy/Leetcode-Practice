# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.ans = True
        def dfs(root):
            if not root: return 0
            else:
                left = dfs(root.left)
                right = dfs(root.right)
                if abs(left-right) > 1:
                    self.ans = False
                return 1 + max(left, right)
           
        dfs(root)

        return self.ans
            

            