# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node):
            if not node:
                return 0
            

            l_max = dfs(node.left)
            r_max = dfs(node.right)

            if l_max ==-1 or r_max ==-1:
                return -1

            if abs(l_max - r_max )>1 :
                return -1

            return 1+ max(l_max, r_max)

        if dfs(root)!= -1:
            return True 
        

        return False 
             

          
            
        