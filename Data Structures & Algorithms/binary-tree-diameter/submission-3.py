class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        m_d = 0

        def dfs(node):
            nonlocal m_d

            if not node:
                return 0

            l_max = dfs(node.left)
            r_max = dfs(node.right)

            m_d = max(m_d, l_max + r_max)

            return 1 + max(l_max, r_max)

        dfs(root)

        return m_d