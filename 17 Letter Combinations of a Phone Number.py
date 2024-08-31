class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if digits == "":
            return []
        self.result = []
        self.path = ""
        self.digit_to_letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.backtracking(digits, 0)
        return self.result

    def backtracking(self, digits, startIdx):
        if len(self.path) == len(digits):
            self.result.append(self.path[:])
            return
        for i in range(startIdx, len(digits)):
            for j in range(len(self.digit_to_letters[digits[i]])):
                self.path += self.digit_to_letters[digits[i]][j]
                self.backtracking(digits, i+1)
                self.path = self.path[:-1]