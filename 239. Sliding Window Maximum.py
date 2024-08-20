# 这个不行，会超时
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        the_max = []
        if (len(nums) == 1):
            the_max.append(nums[0])
        elif (len(nums) < k):
            the_max.append(max(nums[0]))
        else:
            t1 = 0
            t2 = k
            while(t2 <= len(nums)):
                temp = max(nums[t1: t2])
                the_max.append(max(nums[t1:t2]))
                t1 += 1
                t2 += 1
        return the_max
    
    
from collections import deque


class MyQueue:
    def __init__(self):
        self.queue = deque()

    def pop(self, value):
        if self.queue and value == self.queue[0]:
            self.queue.popleft()

    def push(self, value):
        while self.queue and value > self.queue[-1]:
            self.queue.pop()
        self.queue.append(value)

    def front(self):
        return self.queue[0]

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        que = MyQueue()
        result = []
        for i in range(k):
            que.push(nums[i])
        result.append(que.front())
        for i in range(k, len(nums)):
            que.pop(nums[i-k])
            que.push(nums[i])
            result.append(que.front())

        return result

            
                