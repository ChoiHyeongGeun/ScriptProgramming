# 5.46

# math 모듈 사용
import math

# 숫자를 입력하라는 메시지 출력
print("10개의 숫자를 입력하세요 : ")

# 10개의 숫자들의 합
sum = 0

# 10개의 숫자들의 제곱의 합
sum2 = 0

# 10번 반복한다.
for x in range(0, 10) :

    # 숫자를 입력받는다.
    num = eval(input())

    # 숫자들을 합한다.
    sum = sum + num

    # 숫자들을 제곱해서 합한다.
    sum2 = sum2 + (num ** 2)

# 평균
average = sum / 10

# 표준편차
deviation = math.sqrt((sum2 - ((sum ** 2) / 10)) / 9)

# 결과를 출력한다.
print("평균은", average, "입니다.")
print("표준 편차는", deviation, "입니다.")
