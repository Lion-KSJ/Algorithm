input=5
value=5
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0

for start in range(input):
    while interval_sum < value and end < input:
        interval_sum += data[end]
        end += 1

    if interval_sum == value:
        count += 1
    interval_sum -= data[start]

print(count)
    
#병합정렬
n, m = 3,4
a = [1,3,5]
b = [2,4,6,8]

result = [0]*(n+m)

i, j, k = 0, 0, 0

while i<n or j<m:
    if j >= m or (i<n and a[i] <= b[j]):
        result[k] = a[i]
        i+=1
    else:
        result[k] = b[j]
        j+=1
    k+=1

for i in result:
    print (i, end=' ')



