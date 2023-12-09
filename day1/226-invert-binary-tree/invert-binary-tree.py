# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if not root:
            return None

        stack = []

        stack.append(root)

        while stack:
            curr = stack.pop()

            temp = curr.left
            curr.left = curr.right
            curr.right = temp 

            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)

        return root

        

        # --- DFS Recursively ---
        # if not root: 
        #     return None

        # temp = root.left
        # root.left = root.right
        # root.right = temp

        # self.invertTree(root.left)
        # self.invertTree(root.right)

        # return root