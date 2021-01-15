n=3
m=4

array = [[0] * m for _ in range(n)]

print(array)
array[1][1]=1
print(array)

array = [[0]*m]*n
array[1][1]=1
print(array)


a=[1,4,3,5]

print("기본 리스트",a)

a.append(2)
print("리스트 추가",a)

a.sort()
print("리스트 정렬",a)

a.sort(reverse = True)
print("리스트 정렬",a)

a.reverse()
print("리스트 뒤집기",a)

a.insert(2,3)
print("2 3 insert", a)

print("값이  3인 데이터 개수 -> ", a.count(3))

a.remove(2)
print("2 value delete -> ", a)


a = [1,2,3,4,5,5,5]
remove_set={3,5}

result = [i for i in a if i not in remove_set]
print(result)