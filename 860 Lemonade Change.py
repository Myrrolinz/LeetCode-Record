class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        cash = [0, 0, 0]
        for i in range(len(bills)):
            if bills[i] == 5:
                cash[0] += 1
                # print(f"cash[0]: {cash[0]}; cash[1]: {cash[1]}; cash[2]: {cash[2]};")
            if bills[i] == 10:
                cash[1] += 1
                if cash[0] > 0:
                    cash[0] -= 1
                else:
                    return False
                # print(f"cash[0]: {cash[0]}; cash[1]: {cash[1]}; cash[2]: {cash[2]};")
            if bills[i] == 20:
                cash[2] += 1
                if cash[1] > 0 and cash[0] > 0:
                    cash[1] -= 1
                    cash[0] -= 1
                elif cash[0] >= 3:
                    cash[0] -= 3
                else:
                    return False
                # print(f"cash[0]: {cash[0]}; cash[1]: {cash[1]}; cash[2]: {cash[2]};")
        return True

                    