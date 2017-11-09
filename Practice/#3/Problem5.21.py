# 5.21

# math 모듈 사용
import math

# 피라미드가 총 8줄
max = 8

# 8번 반복한다.
for x in range(0, max) :

    # 층마다 띄어서 출력하기 위한 공백
    # 높은 층일수록 많이 띄어서 출력한다.
    for z in range(0, max-1-x) :

        print(end = '     ')

    # 내용 출력
    for y in range(0, 2*(x+1)-1) :

        # 중간까지는 값이 증가한다.
        if y <= math.ceil(((2*(x+1)-1) / 2) - 1) :

            print(format(2 ** y, "4.0f"), end = ' ')

        # 중간 이후부터는 값이 다시 감소한다.
        else :

            print(format(2 ** (2*(x+1)-1-y-1), "4.0f"), end = ' ')

    print() # 다음 줄로
