n = int(input())
data = []
result = []
for i in range(n):
    data.append(int(input()))
while data != []:
    min = data[0]
    for j in range(len(data)):
        if data[j] < min:
            min = data[j]
    data.remove(min)
    print(min)