data = input()
result = set()

for i in range(len(data)):
    for j in range(i+1, len(data)+1):
        result.add(data[i:j])

print(len(result))