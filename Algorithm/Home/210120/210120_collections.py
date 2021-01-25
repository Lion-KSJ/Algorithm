#deque에서 
# 첫번째 원소를 제거할 때 -> popleft()
# 마지막 원소를 제거할 때 -> pop()
# 첫번째 인덱스에 원소 x를 삽입할 때 -> appendleft(x)
# 마지막 인덱스에 원소를 삽입할 때 -> append(x)

# deque를 사용해 삽입할땐 append(), 삭제할때는 popleft()를 사용한다

from collections import deque

data = deque([2,3,4])
print("삽입")
print(data)
data.appendleft(1)
print(data)
data.append(5)
print(data)

print("삭제")
data.popleft()
print(data)
data.pop()
print(data)

# 

from collections import Counter

counter = Counter(['red', 'blue', 'red', 'green', 'blue', 'blue'])
print("blue -> ", counter['blue'])
print("red -> ", counter['red'])
print(dict(counter))

data = list([1,2,3,4,5,6,8,7,1,32,1,5,5,7,52,6,8,2,3,2,9,8,4,3,23,4,89,5,2,1])
data = sorted(data)
counter = Counter(data)
print(data)
print(counter[3])
print(dict(counter))
print(counter[89])