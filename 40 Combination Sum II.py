class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.result = []
        self.path = []
        candidates = sorted(candidates)
        self.backtracking(candidates, target, 0)
        # self.result = self.process_nested_list(self.result)
        return self.result

    def backtracking(self, candidates, target, startIdx):
        if sum(self.path) >= target:
            if sum(self.path) == target and self.path not in self.result:
                self.result.append(self.path[:])
            return

        for i in range(startIdx, len(candidates)):
            # 下面这俩if是不超限的关键
            if i > startIdx and candidates[i] == candidates[i-1]:
                continue
            if sum(self.path) + candidates[i] > target:
                break
            self.path.append(candidates[i])
            self.backtracking(candidates, target, i+1)
            self.path.pop()

        
    # def process_nested_list(self, nested_list):
    #     # 对每个子列表进行排序和去重
    #     processed_list = [sorted(sub_list) for sub_list in nested_list]
    #     # print(processed_list)
    #     # 将整个列表去重并排序
    #     unique_sorted_list = sorted(set(tuple(sub_list) for sub_list in processed_list))
    #     # print(unique_sorted_list)
    #     # 将元组再转换回列表
    #     return [list(t) for t in unique_sorted_list]
