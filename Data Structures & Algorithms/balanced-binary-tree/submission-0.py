# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def helper(node):
            if not node:
                return 0, True
            lh, lb = helper(node.left)
            rh, rb = helper(node.right)

            b = lb and rb and abs(lh-rh)<=1
            h = max(lh,rh)+1

            return h, b
        _, result = helper(root)
        return result 


            
        