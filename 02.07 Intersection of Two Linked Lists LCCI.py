# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA == None or headB == None:
            return None
        cntA = 1
        cntB = 1
        curr = headA
        while curr.next:
            cntA += 1
            curr = curr.next
        curr = headB
        while curr.next:
            cntB += 1
            curr = curr.next

        p1 = headA
        p2 = headB
        if cntA > cntB:
            for i in range(cntA-cntB):
                p1 = p1.next
            for i in range(cntB):
                if p1 == p2:
                    return p1
                else:
                    p1 = p1.next
                    p2 = p2.next
        else:
            for i in range(cntB-cntA):
                p2 = p2.next
            for i in range(cntA):
                if p1 == p2:
                    return p1
                else:
                    p1 = p1.next
                    p2 = p2.next

        return None
        

        