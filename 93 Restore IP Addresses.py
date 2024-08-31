class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        self.result = []
        self.path = []
        self.sub_s = ""
        self.backtracking(s, 0, 0)
        return self.result

    def backtracking(self, s, startIdx, now_split):
        print(".".join(self.path))
        if "".join(self.path) == s and now_split == 4:
            print(self.path)
            self.result.append(".".join(self.path))
            return

        for i in range(startIdx+1, len(s)+1):
            if now_split >= 4:
                return
            self.sub_s = s[startIdx: i]
            now_split += 1
            # print(self.sub_s)
            if self.is_valid(self.sub_s):
                self.path.append(self.sub_s)
                self.backtracking(s, i, now_split)
                self.path.pop()
                now_split -= 1

    def is_valid(self, s):
        if len(s) > 1 and s[0] == '0':
            return False
        if int(s) > 255:
            return False
        return True