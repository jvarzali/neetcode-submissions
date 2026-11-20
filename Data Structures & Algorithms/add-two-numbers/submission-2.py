# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def sumList(curr: Optional[ListNode]) -> int:
            sol = 0
            digit = 0
            while curr:
                sol += curr.val * (10 ** digit)
                curr = curr.next
                digit += 1

            return sol

        ans = sumList(l1) + sumList(l2)
        head = ListNode(0)
        curr = head

        if ans == 0:
            return head

        while ans > 0:
            curr.next = ListNode(ans % 10)
            curr = curr.next
            ans = ans // 10

        return head.next
