# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def height( root: Optional[TreeNode]) -> bool:
            if root is None: return 0

            left_h = height(root.left)
            right_h = height(root.right)

            if left_h < 0 or right_h <0 or abs(left_h-right_h) > 1 : return -1

            return max(left_h, right_h) + 1

        return (height(root) >= 0)