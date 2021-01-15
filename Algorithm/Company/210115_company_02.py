import sys

data = sys.stdin.readline().rstrip()
print(data)

def add(a,b):
    print("Add Function -> ", a+b)

add(3,4)

a=0
b=0
def func():
    global a
    a += 1

for i in range(10):
    func()

print(a, b)

def add_1(a,b):
    return a+b

print((lambda a,b: a+b)(3,17))

# 입출력
n = int(input())
data = list(map(int, input().split()))

data.sort(reverse=True)
print(data)

n, m, k =map(int, input().split())

print(n, m, k)




