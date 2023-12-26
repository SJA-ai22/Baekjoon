data = input().upper()
data_list = list(set(data))
max = 0
max_str ='?'

for i in data_list:
    if(data.count(i) > max):
        max = data.count(i)
        max_str = i
    elif(data.count(i) == max):
        max_str = '?'
print(max_str)