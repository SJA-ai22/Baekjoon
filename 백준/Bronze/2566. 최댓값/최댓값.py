data = []
max = 0
row, col = 0, 0
for i in range(9):
    data.append(list(map(int, input().split())))
for n in range(9):
    for m in range(9):
        if max <= data[n][m]:
            max = data[n][m]
            row = n+1
            col = m+1
print(max)
print(row, col)