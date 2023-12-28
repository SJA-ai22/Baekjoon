row, col = map(int, input().split())
A = []
B = []
for i in range(row):
    A.append(list(input().split()))
for j in range(row):
    B.append(list(input().split()))
for n in range(row):
    for m in range(col):
        print(int(A[n][m]) + int(B[n][m]), end=' ')
    print()