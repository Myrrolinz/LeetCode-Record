class Solution:
    def isHappy(self, n: int) -> bool:
        happy = set()
        while n != 1:
            n = sum(int(i) ** 2 for i in str(n))
            if n in happy:
                return False
            else:
                happy.add(n)

        return True
    
    # 这题不会，抄的，实际上就是hash