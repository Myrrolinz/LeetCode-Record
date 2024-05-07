class MyStack:

    def __init__(self):
        self.que = deque()


    def push(self, x: int) -> None:
        self.que.append(x)


    def pop(self) -> int:
        if self.empty():
            return None
        else:
            for i in range(len(self.que) - 1):
                self.que.append(self.que.popleft())
            ans = self.que.popleft()
            return ans


    def top(self) -> int:
        ans = self.pop()
        if ans:
            self.que.append(ans)
        return ans


    def empty(self) -> bool:
        if self.que:
            return False
        else:
            return True



# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()