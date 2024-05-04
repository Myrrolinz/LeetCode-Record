def generateMatrix(n: int):
    nums = [[0] * n for _ in range(n)]
    loop = n // 2 
    cnt = 1
    for i in range(loop):
        for j in range(i, n - 1 - i):
            nums[i][j] = cnt
            cnt += 1
        for j in range(i, n - 1 - i):
            nums[j][n-i-1] = cnt
            cnt += 1
            
        # tmp = [temp for temp in range(n-i-1, i, -1)]
        # print(f"tmp: {tmp}")
        # print(range(i+1, n-i, -1))
        # print(range(n-i-1, i, -1))
        for j in range(n-i-1, i, -1):
            print(f"n-i-1: {n-i-1}, j: {j}")
            nums[n-i-1][j] = cnt
            cnt +=1
        for j in range(n-i-1, i, -1):
            print(f"j: {j}, i: {i}")
            nums[j][i] = cnt
            cnt +=1
    print(n//2)
    if n % 2 == 1:
        nums[n//2][n//2] = cnt
    return nums

n = 3
print(generateMatrix(n))