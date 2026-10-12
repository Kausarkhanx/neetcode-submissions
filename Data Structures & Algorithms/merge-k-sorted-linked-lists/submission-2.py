# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if len(lists) == 0:
            return None

        while len(lists) > 1:
            new_lists = []

            for i in range(0, len(lists), 2):
                list1 = lists[i]

                if i + 1 < len(lists):
                    list2 = lists[i + 1]
                else:
                    list2 = None

                merged = self.mergeTwoLists(list1, list2)
                new_lists.append(merged)

            lists = new_lists

        return lists[0]
    
    def mergeTwoLists(self, list1, list2):
        if list1 is None and list2 is None:
            return None
            
        if list1 is None:
            return list2

        if list2 is None:
            return list1

        dummy = ListNode()
        head = dummy

        while list1 is not None and list2 is not None:

            if list1.val <= list2.val:
                head.next = list1
                list1 = list1.next

            else:
                head.next = list2
                list2 = list2.next

            head = head.next

        if list1 is not None:
            head.next = list1
        else:
            head.next = list2

        return dummy.next