class Solution:
    def isSubtree(self, r, sr):

        def dfs(a, b):
            if not a and not b:
                return True

            if not a or not b:
                return False

            if a.val != b.val:
                return False

            return (
                dfs(a.left, b.left)
                and
                dfs(a.right, b.right)
            )

        if not sr:
            return True

        if not r:
            return False

        if dfs(r, sr):
            return True

        return (
            self.isSubtree(r.left, sr)
            or
            self.isSubtree(r.right, sr)
        )