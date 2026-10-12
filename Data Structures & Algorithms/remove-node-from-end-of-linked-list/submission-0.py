# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        # find the length of the linked list
        length = 0 
        curr_node = head
        
        while curr_node != None:
            length = length+1
            curr_node = curr_node.next
        #print(length)

        node_to_remove = length - n

        if node_to_remove == 0:
            # this is head which we are removing, so return tail which will be the new head
            return head.next

        curr_node = head

        for i in range(node_to_remove - 1):
            # need to find the node before 'n' and the node after 'n'
            # curr_node -> node_to_remove -> next_node
            curr_node = curr_node.next
        curr_node.next = curr_node.next.next
        return head
            
