import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        map_ = {}
        for i in range(len(nums)):
            map_[nums[i]] = map_.get(nums[i], 0) + 1

        pri_que = []
        for key, value in map_.items():
            # heappush用法：如果第一个元素相同，才会继续比较第二个元素（即 key）。
            heapq.heappush(pri_que, (value, key))
            if len(pri_que) > k:
                heapq.heappop(pri_que)

        result = [0] * k
        for i in range(k-1, -1, -1):
            result[i] = heapq.heappop(pri_que)[1]

        return result