#정수형
a = 1000
b =-7
c= 0

print("1. 정수형 -> ", a ,b, c)

#실수형

#양의 정수
a=157.93
#음의 정수
b=-1837.2
#소수부가 0일때
c=5.
#정수부가 0일때
d=-.7
print("2. 실수형 -> ", a ,b, c, d)

#10이상의 지수 표현
a = 1e9
# 752.5
b=75.25e1
# 3.954
c=3954e-3
# TEST3
d=3954e3
print("3. 지수 표현 -> ", a ,b, c, d)

#실수 계산 시 저장 방식
a=0.3+0.6

if a==0.9:
    print(True, "-> 4. Result : " , a)
else:
    print(False, "-> 4. Result : " , a) 

# round 함수
roundResult = round(a,1)
if roundResult == 0.9:
    print(True, "-> 5. round Result : " , roundResult)
else:
    print(False, "-> 5. round Result : " , roundResult) 

#자료형 연산
a=8
b=2

print("6. 나누기 -> ", a/b)
print("6. 나머지 -> ", a%b)
print("6. 몫 -> ", a//b)

# 거듭제곱
a=5
b=3
print("7. 거듭제곱 -> ", a**b)

# 리스트
a=[1,2,3,4,5,6,7,8,9,10]
print("10. 리스트 -> ", a)
print("10. 리스트 -> ", a[4])
a = list()
print("10. 리스트 선언 1-> ", a)
a = []
print("10. 리스트 선언 2-> ", a)

n=10
a=[0]*n
print("10. 리스트 초기화 -> ",a)

# 리스트 인덱싱과 슬라이싱
a=[1,2,3,4,5,6,7,8,9,10]
print("11. 리스트 -> ", a)
print("11. 리스트 인자 -1 -> ",a[-1])
print("11. 리스트 인자 -3 -> ",a[-3])
a[3]=7
print("11. 리스트 인자 3 -> ",a[3])
print("11. 리스트 -> ", a)

print("11. 리스트 슬라이싱 -> ", a[1:4])

# 리스트 컴프리헨션 -> 초기화하는 방법
array = [i for i in range(20) if i%2 ==1]

print("12. 리스트 초기화 -> ", array)
lenA = len(a)
array = [i*i for i in range(1,10)]
print("12. 리스트 초기화 -> ", array)

