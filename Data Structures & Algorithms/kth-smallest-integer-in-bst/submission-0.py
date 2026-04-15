# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        c = 0
        r = None

        def h(node):
            nonlocal c
            nonlocal r

            if not node or r is not None:
                return 

            h(node.left)

            c+=1
            if c ==k:
                r = node.val
                return 
            
            h(node.right)
        h(root)
        return r

    
        
        