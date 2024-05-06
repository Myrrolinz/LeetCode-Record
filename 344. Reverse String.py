class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        len_ = len(s) - 1
        for i in range(len(s) // 2):
            temp = s[i]
            s[i] = s[len_ -i]
            s[len_-i] = temp
            # 更简洁的写法：
            # s[i], s[n - i - 1] = s[n - i - 1], s[i]
        return s