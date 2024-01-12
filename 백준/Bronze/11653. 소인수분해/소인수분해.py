num = int(input())
data = []
for i in range(2,num+1):
    while num % i == 0:
        data.append(i)
        num = num/i

for j in range(len(data)):
    print(data[j])
