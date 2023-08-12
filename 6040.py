# 본 문제는python의 빠른 기초 학습을 위해 설계된 문제로서python코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 2개(a, b) 를 입력받아 a를 b로 나눈 몫을 출력해보자.

# 예시
# ...
# print(a//b)

# 참고
# python언어에서는 나눈 몫을 계산하는 연산자(//, floor division)를 제공한다.
# a//b 와 같이 작성하면, a를 b로 나눈 몫(quotient)을 계산해준다.
# 프로그래밍언어에 따라 이렇게 몫을 계산해주는 연산자가 없는 경우도 있다.

# 실수로 나눈 몫이 어떻게 계산될지도 생각해보자.

x, y = input().split()
print(int(x)//int(y))