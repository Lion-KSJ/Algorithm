from itertools import permutations

data = ['A', 'B', 'C']
#모든 순열 구하기
result  = list(permutations(data,3))
count =  len(result)
print("permutations-> ", result, count)

from itertools import combinations
data = ['A', 'B', 'C']
#2개를 뽑는 모든 조합 구하기
result = list(combinations(data,2))
count =  len(result)
print("combinations ->", result, count)

from itertools import product

data = ['A', 'B', 'C']
#2개를 뽑는 모든 순열 구하기(중복허용)
result = list(product(data, repeat = 2))
print("product ->", result, len(result))

from itertools import combinations_with_replacement

data = ['A', 'B', 'C']
#2개를 뽑는 모든 조합 구하기(중복허용)
result = list(combinations_with_replacement(data,2))
print("product ->", result, len(result))