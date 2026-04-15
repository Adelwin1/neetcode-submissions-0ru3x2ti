# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.mh = 0

        def height(men):
            if not men:
                return 0
            
            lh = height(men.left)
            rh = height(men.right)

            self.mh = max(self.mh, lh+rh)
            return max(lh, rh)+1

        height(root)
        return self.mh
