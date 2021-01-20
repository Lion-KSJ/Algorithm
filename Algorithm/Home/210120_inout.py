# 한칸씩 띄워진거 but 입력 수가 많으면 느려짐
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse = True)
print(data)

# 한줄 받기
import sys
data = sys.stdin.readline().rstrip()
print(data)

# 문자 사이에 숫자 출력할떄
result = 7
print("정답은 " + str(result) + " 입니다.")
print("정답은",str(result),"입니다.")
print(f"정답은 {result} 입니다.")