# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        global res
        res = 0 

        def dfs(root, h):
            global res
            if not root: return 0

            l = dfs(root.left, h)
            r = dfs(root.right, h)

            res = max(res, l+1 , r+1)

            return max(l,r) + 1

        dfs(root, 0)

        return res

