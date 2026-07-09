# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode()
        p1, p2 = list1, list2

        curr = head

        while p1 != None or p2 != None:
            if p1 == None:
                temp = p2.next
                p2.next = None
                curr.next = p2
                p2 = temp
            elif p2 == None or p1.val < p2.val:
                temp = p1.next
                p1.next = None
                curr.next = p1
                p1 = temp
            else:
                temp = p2.next
                p2.next = None
                curr.next = p2
                p2 = temp

            curr = curr.next
        
        return head.next

            


