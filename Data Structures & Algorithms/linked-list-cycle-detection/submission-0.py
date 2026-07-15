# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        end = ListNode("end")

        while head != None:
            if head.val == "end":
                return True
            curr = head
            head = head.next
            curr.next = end

        return False