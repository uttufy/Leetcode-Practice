# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def dfs(root, s):
            if not root and not s:
                return True
            if not root or not s:
                return False   
            return root.val == s.val and dfs(root.right, s.right) and dfs(root.left, s.left)

        if not root: return 
        if not root: return False
        if root.val==subRoot.val and dfs(root,subRoot): return True
        return self.isSubtree(root.left,subRoot) or self.isSubtree(root.right, subRoot)
            
       