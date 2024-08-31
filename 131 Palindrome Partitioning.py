class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.result = []
        self.path = []
        self.sub_s = ""
        self.backtracking(s, 0)
        return self.result

    def backtracking(self, s, startIdx):
        if "".join(self.path) == s:
            # print(self.path)
            self.result.append(self.path[:])
            return

        for i in range(startIdx+1, len(s)+1):
            self.sub_s = s[startIdx: i]
            # print(self.sub_s)
            if self.is_palindrome(self.sub_s):
                self.path.append(self.sub_s)
                self.backtracking(s, i)
                self.path.pop()

    def is_palindrome(self, s):
        # 直接比较字符串和它的反转
        return s == s[::-1]