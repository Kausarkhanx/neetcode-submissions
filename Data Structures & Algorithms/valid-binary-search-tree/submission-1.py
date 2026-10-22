# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode], low=float("-inf"), high=float("inf")) -> bool:
        if root == None:
            return True
        
        # constraints
        if root.val <= low or root.val >= high:
            return False
        
        left_side = self.isValidBST(root.left, low, root.val) #root must be greater than the left child
        right_side = self.isValidBST(root.right, root.val, high)

        return left_side and right_side