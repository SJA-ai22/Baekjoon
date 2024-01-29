data = []
result = []
mean = 0
for i in range(5):
    a = int(input())
    data.append(a)
    mean += a
print(int(mean/5))
while data != []:
    min = data[0]
    for j in range(len(data)):
        if data[j] < min:
            min = data[j]
    data.remove(min)
    result.append(min)
print(result[2])