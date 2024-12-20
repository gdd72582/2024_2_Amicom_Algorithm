# 1로 만들기
def make_one(n):
    D = [0] *(n+1)
    for i in range(2, n+1):
        D[i] = D[i-1] + 1
        if i % 2 == 0: D[i] = min(D[i], D[i//2] + 1)
        if i % 3 == 0: D[i] = min(D[i], D[i//3] + 1)
    return D[n]

n = int(input())
print(make_one(n))