# 3.4

# math 모듈 사용
import math

# 한 변의 길이를 입력받는다.
s = eval(input("한 변의 길이를 입력하세요 : "))

# 넓이를 식에 맞게 계산한다.
w = (5 * s * s) / (4 * math.tan(math.pi / 5))

# 결과를 출력한다.
print("오각형의 넓이는", w, "입니다.")
