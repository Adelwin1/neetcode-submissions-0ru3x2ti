# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        count = 0
        def h(node, m):
            nonlocal count
            if not node:
                return  
            if node.val >= m:
                count+=1
            nm = max(m , node.val)
            h(node.left, nm)
            h(node.right, nm)
        h(root, root.val)
        return count
        
        

        