# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        def h(node, level):
            if not node:
                return 
        
            if level ==len(result):
                result.append(node.val)
            h(node.right, level+1)
            h(node.left, level+1)

        h(root, 0)
        return result



        