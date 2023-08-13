# 본 문제는 python 의 빠른 기초 학습을 위해 설계된 문제로서 python 코드 제출을 기준으로 설명되어 있습니다. 
# ------

# 정수 1개를 입력받아 2배 곱해 출력해보자.

# 참고
# *2 를 계산한 값을 출력해도 되지만,
# 정수를 2배로 곱하거나 나누어 계산해 주는 비트단위시프트연산자 <<, >>를 이용할 수 있다.
# 컴퓨터 내부에는 2진수 형태로 값들이 저장되기 때문에,
# 2진수 형태로 저장되어 있는 값들을 왼쪽(<<)이나 오른쪽(>>)으로
# 지정한 비트 수만큼 밀어주면 2배씩 늘어나거나 1/2로 줄어드는데,

# 왼쪽 비트시프트(<<)가 될 때에는 오른쪽에 0이 주어진 개수만큼 추가되고,
# 오른쪽 비트시프트(>>)가 될 때에는 왼쪽에 0(0 또는 양의 정수인 경우)이나 1(음의 정수인 경우)이 개수만큼 추가되고,
# 가장 오른쪽에 있는 1비트는 사라진다.

# 예시
# n = 10
# print(n<<1)  #10을 2배 한 값인 20 이 출력된다.
# print(n>>1)  #10을 반으로 나눈 값인 5 가 출력된다.
# print(n<<2)  #10을 4배 한 값인 40 이 출력된다.
# print(n>>2)  #10을 반으로 나눈 후 다시 반으로 나눈 값인 2 가 출력된다.

# 정수 10의 2진수 표현은 ... 1010 이다.
# 10 << 1 을 계산하면 ... 10100 이 된다 이 값은 10진수로 20이다.
# 10 >> 1 을 계산하면 ... 101 이 된다. 이 값은 10진수로 5이다.

# n = 10 과 같이 키보드로 입력받지 않고 직접 작성해 넣은 코드에서, 숫자로 시작하는 단어(식별자, identifier)는 자동으로 수로 인식된다.  

# n = 10 에서 10 은 10진수 정수 값으로 인식된다.
# 변수 n 에 문자열을 저장하고 싶다면, n = "10" 또는 n = '10'으로 작성해 넣으면 되고,

# n = 10.0 으로 작성해 넣으면 자동으로 실수 값으로 저장된다.
# n = 0o10 으로 작성해 넣으면 8진수(octal) 10으로 인식되어 10진수 8값이 저장되고,
# n = 0xf 나 n = 0XF 으로 작성해 넣으면 16진수(hexadecimal) F로 인식되어 10진수 15값으로 저장된다.

# ** python에서 실수 값에 대한 비트시프트 연산은 허용되지 않고 오류가 발생한다.
# (실수 값도 컴퓨터 내부적으로는 2진수 형태로 저장되고 비트시프트 처리가 될 수 있지만, python 에서는 허용하지 않는다.)

x = input()
x = int(x)
print(x<<1)