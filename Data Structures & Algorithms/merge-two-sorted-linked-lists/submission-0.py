# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = None
        p1, p2 = list1, list2

        if p1 == None and p2 == None:
            return None
        elif p1 == None:
            temp = p2.next
            p2.next = None
            head = p2
            p2 = temp
        elif p2 == None or p1.val < p2.val:
            temp = p1.next
            p1.next = None
            head = p1
            p1 = temp
        else:
            temp = p2.next
            p2.next = None
            head = p2
            p2 = temp

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
        
        return head

            


