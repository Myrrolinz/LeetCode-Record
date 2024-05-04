class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class MyLinkedList:
    def __init__(self):
        self.dummy_head = ListNode()
        self.size = 0

    def get(self, index: int) -> int:
        # 这句非常重要，<0 或者 >= size 的判断
        if index < 0 or index >= self.size:
            return -1
        else:
            curr = self.dummy_head.next
            for i in range(index):
                curr = curr.next
        return curr.val

    def addAtHead(self, val: int) -> None:
        new_head = ListNode(val=val,next=self.dummy_head.next)
        self.dummy_head.next = new_head
        self.size += 1

    def addAtTail(self, val: int) -> None:
        new_tail = ListNode(val=val)
        curr = self.dummy_head
        while curr.next:
            curr = curr.next
        curr.next = new_tail
        self.size += 1


    def addAtTail(self, val: int) -> None:
        current = self.dummy_head
        while current.next:
            current = current.next
        current.next = ListNode(val)
        self.size += 1


    def addAtIndex(self, index: int, val: int) -> None:
        # new_node = ListNode(val=val)
        if index < 0 or index > self.size:
            return -1
        if index == 0:
            self.addAtHead(val)
        elif index == self.size:
            self.addAtTail(val)
        else:
            curr = self.dummy_head
            new_node = ListNode(val=val)
            for i in range(index):
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:
            return -1
        curr = self.dummy_head
        for i in range(index):
            curr = curr.next
        curr.next = curr.next.next
        self.size -= 1



# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)