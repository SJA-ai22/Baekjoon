data = []
result = ''
for i in range(5):
    data.append(list(input()))
for j in range(15):
    for k in range(5):
        if j < len(data[k]):
            result += data[k][j]
print(result)