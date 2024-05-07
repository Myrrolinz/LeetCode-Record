class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        cal = []
        for i in tokens:
            if i.isdigit():
                cal.append(i)
                # print(cal)
            elif i == '+':
                num2 = cal.pop()
                num1 = cal.pop()
                cal.append(int(num1) + int(num2))
                # print(cal)
            elif i == '-' and len(i) == 1:
                num2 = cal.pop()
                num1 = cal.pop()
                cal.append(int(num1) - int(num2))
                # print(cal)
            elif i == '*' :
                num2 = cal.pop()
                num1 = cal.pop()
                cal.append(int(num1) * int(num2))
                # print(cal)
            elif i == '/':
                num2 = cal.pop()
                num1 = cal.pop()
                cal.append(int(num1) / int(num2))
                # print(cal)
            else:
                cal.append(i)
                # print(cal)
        return int(cal[-1])