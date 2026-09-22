# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        max_h = 1

        def dfs(node):
            if not node:
                return 0
            
            

            l_max = dfs(node.left)
            r_max =dfs(node.right)


            return 1+ max(l_max, r_max)
        return dfs(root)

    