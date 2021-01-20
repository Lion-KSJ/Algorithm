result = sum([1,2,3,4,5])
print(result)

result = min(7,3,5,9,4,2,4,8)
print(result)

result = max(7,3,5,9,4,2,4,8)
print(result)

result = eval("(3+5)*7")
print(result)

result = sorted([9,5,4,7,2,1,5,3,7,1,0])
print(result)

result = sorted({9,5,4,7,2,1,5,3,7,1,0})
print(result)

result = sorted([9,5,4,7,2,1,5,3,7,1,0], reverse = True)
print(result)

result = sorted({9,5,4,7,2,1,5,3,7,1,0}, reverse = True)
print(result)

result = sorted([('김성제',50),('이상엽',80),('박지용',100)], key = lambda x:x[1])
print(result)

result = sorted([('김성제',50),('이상엽',80),('박지용',100)], key = lambda x:x[0])
print(result)

result = sorted([('김성제',50),('이상엽',80),('박지용',100)], key = lambda x:x[1], reverse =True)
print(result)

result = sorted([('김성제',50),('이상엽',80),('박지용',100)], key = lambda x:x[0], reverse =True)
print(result)


