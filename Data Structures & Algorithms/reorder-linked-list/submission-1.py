# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return

        fast = head
        slow = head
        temp = None
        
        while fast and fast.next:
            fast = fast.next.next
            temp = slow
            slow = slow.next

        temp.next = None
        prev = None
        curr = slow
        post = slow.next

        while post:
            curr.next = prev
            prev = curr
            curr = post
            post = post.next

        curr.next = prev
        back = curr
        front = head

        final = front
        curr = final
        front = front.next

        while front and back:
            curr.next = back
            curr = curr.next
            back = back.next
            curr.next = front
            curr = curr.next
            front = front.next

        while back:
            curr.next = back
            curr = curr.next
            back = back.next

        head = final

        
        
        