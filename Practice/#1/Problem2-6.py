# 2.6 : 정수의 자릿수 합산하기

# 0~1000 사이의 숫자를 입력받는다.
number = eval(input("0과 1000 사이의 숫자를 입력하세요 : "))

# 1의 자리 숫자
num1 = number % 10

# 10의 자리 숫자
num2 = (number - num1) % 100

# 100의 자리 숫자
num3 = (number - num1 - num2) % 1000

# 1000의 자리 숫자
num4 = (number - num1 - num2 - num3) % 10000

# 모든 자리 숫자들의 합
result = num1 + (num2 / 10) + (num3 / 100) + (num4 / 1000)

# 결과를 출력한다.
print("각 자릿수의 합은", int(result), "입니다.")
