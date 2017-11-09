# 2.13 : 숫자 분할하기

# 4자리 정수를 입력받는다.
number = eval(input("4자리 정수를 입력하세요 : "))

# 1의 자리 숫자
num1 = number % 10

# 10의 자리 숫자
num2 = ((number - num1) % 100) / 10

# 100의 자리 숫자
num3 = ((number - num1 - num2) % 1000) / 100

# 1000의 자리 숫자
num4 = ((number - num1 - num2 - num3) % 10000) / 1000

# 결과를 출력한다.
print(int(num4))
print(int(num3))
print(int(num2))
print(int(num1))
