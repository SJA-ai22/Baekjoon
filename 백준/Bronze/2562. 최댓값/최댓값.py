data = []
for i in range(9):
    data.append(int(input()))

max_value = data[0]
num = 1

for j in range(9):
    if max_value < data[j]:
        max_value = data[j]
        num = j + 1

print(max_value)
print(num)