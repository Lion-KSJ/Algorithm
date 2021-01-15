a = set([1,2,3,4,5])
b = set([1,1,1,2,3,5,4,4,5])

print(a)
print(b)

b=set([3,4,5,6,7,8])

print("합집합 -> ", a | b)
print("교집합 -> ", a & b)
print("차집합 -> ", a - b)

# if 문
score = 85

if score>=80:
    print("80점 이상")
else:
    print("80점 미만")

if score>=80: result="Success"
else: result="Fail"

print(result)

result = "Success IF Test" if score >=80 else "Fail If Test"
print(result)


remove_set = [3,5]

result=[]
for i in b:
    if i not in remove_set:
        result.append(i)

print("remove_set(3,5) Test B", b, result)

result = [i for i in a if i not in remove_set]
print("remove_set(3,5) Test A", a, result)

# 반복문
i=1
result=0

while i<=9:
    result += i
    i+=1

print("SUM -> ", result)

i=1
result=0
while i<=9:
    if i%2 == 1:
        result += i
    i+=1

print("SUM -> ", result)

for i in range(1,10):
    result=+i

print("for loop Test -> ", result)

score = [90,85,77,65,97,81,83]
lenScore = len(score)
for i in range(lenScore):
    if score[i]>=80:
        print("80점이상이요 -> ", score[i])

black_list={2,4}
print("Score -> ", score)
for i in  range(lenScore):
    if i+1 in black_list:
        continue
    if score[i] >= 80:
        print(i+1, "번은 합격입니다.")