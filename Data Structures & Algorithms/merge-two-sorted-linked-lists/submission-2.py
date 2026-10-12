class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:

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