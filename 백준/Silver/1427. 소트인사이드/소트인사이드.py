num = input()
data = []
result = ''
for i in num:
    data.append(int(i))
data.sort(reverse=True)
for j in data:
    result += str(j)
print(result)