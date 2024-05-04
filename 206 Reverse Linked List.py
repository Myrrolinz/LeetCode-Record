# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head):
        pre = None # important!! if pre.next = head, it will loop forever
        curr = head
        # tmp = curr.next
        while curr:
            tmp = curr.next # important! 如果是末尾才tmp = tmp.next，会在最后一个节点时无法移入到空指针，curr一直true而死循环
            curr.next = pre
            pre = curr
            curr = tmp
            # if tmp.next:
            #     tmp = tmp.next

        return pre