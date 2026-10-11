# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # check for already visited nodes
        curr_node = head
        visited_nodes = set()

        # check until the end of the list
        while curr_node is not None:
            if curr_node in visited_nodes:
                # cycle exists as it's already visited
                return True 
            else:
                # mark curr node as visited 
                visited_nodes.add(curr_node)
                # move curr node ahead
                curr_node = curr_node.next
        return False
