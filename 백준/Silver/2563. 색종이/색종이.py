paper = [[0 for j in range(100)] for i in range(100)]
count = 0;

num = int(input())
for k in range(num):
    row, col = map(int, input().split())
    for n in range(row, row+10):
        for m in range(col, col+10):
            paper[n][m] = 1
for z in paper:
    count += z.count(1)
print(count)