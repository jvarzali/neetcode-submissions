# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        sol = ListNode(None, head)
        curr, end = sol, head

        for i in range(n):
            end = end.next

        while end:
            curr = curr.next
            end = end.next
        
        curr.next = curr.next.next

        return sol.next