N = int(input())
F = 1
bk = 0

for i in range(N):
    temp = bk
    print(F)

    bk = F
    F = temp + F