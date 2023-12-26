num = int(input())
result = 0

for i in range(num):
    found = False
    data = input()
    for j in range(1,len(data)):
        if (data[j] != data[j-1]) and (data[j] in data[0:j]):
            found =True
    if(found):
        result += 1
print(num - result)