# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # we can perform in-order traversal to sort the tree 
        # in-order = left, root, right

        sorted = []

        def inorder(node):
            if node == None:
                return None
            else:
                inorder(node.left)
                sorted.append(node.val)
                inorder(node.right)
        inorder(root)
        return sorted[k-1]
        

                
    