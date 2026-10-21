# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        # check if left and right side is the same
        if p == None and q == None:
            return True
        elif p == None and q != None:
            return False
        elif q == None and p != None:
            return False
        elif p.val != q.val:
            return False
        else:
            # perform recursion
            left_side = self.isSameTree(p.left, q.left) # returns True or False
            right_side = self.isSameTree(p.right, q.right)
            return left_side == True and right_side == True # matches

