class Solution:
    def trap(self, height: List[int]) -> int:
        stack = [0]
        sum = 0
        for i in range(1, len(height)):
            # print(stack)
            while stack and height[i] > height[stack[-1]]:
                mid = stack[-1]
                stack.pop()
                if stack:
                    h = min(height[stack[-1]], height[i]) - height[mid]
                    w = i - stack[-1] - 1
                    sum += h * w
            stack.append(i)

        return sum