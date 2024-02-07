num = int(input())
data = []
for i in range(num):
    a = input()
    if a in data:
        continue;
    else:
        data.append(a)
data.sort()
length = 1
while data:
    new = []
    for j in data:
        if len(j) == length:
            print(j)
        else:
            new.append(j)
    data = new
    length += 1