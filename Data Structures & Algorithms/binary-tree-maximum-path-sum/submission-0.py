class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:

        self.max_sum = float("-inf")

        def dfs(node):

            if node == None:
                return 0

            left = max(dfs(node.left), 0)
            right = max(dfs(node.right), 0)

            current_path = node.val + left + right

            self.max_sum = max(self.max_sum, current_path)

            return node.val + max(left, right)

        dfs(root)

        return self.max_sum