# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def swapPairs(self, head):
        dummy_head = ListNode(next=head)
        curr = dummy_head
        while curr.next and curr.next.next:
            p1 = curr.next
            p2 = curr.next.next
            p3 = curr.next.next.next
            curr.next = p2
            p2.next = p1
            p1.next = p3
            curr = curr.next.next

        return dummy_head.next
            