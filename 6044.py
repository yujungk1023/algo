# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개(a, b)를 입력받아 합, 차, 곱, 몫, 나머지, 나눈 값을 자동으로 계산해보자.
# 단, b는 0이 아니다.

x, y = input().split()
x = int(x)
y = int(y)
print(x+y)
print(x-y)
print(x*y)
print(x//y)
print(x%y)
print(format(x/y, ".2f"))
