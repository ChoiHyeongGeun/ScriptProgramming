# 3.2

# math 모듈 사용
import math

# 첫 번째 점을 입력받는다.
x1, y1 = eval(input("첫 번째 점(위도와 경도)을 60분법 각으로 입력하세요 : "))

# 두 번째 점을 입력받는다.
x2, y2 = eval(input("두 번째 점(위도와 경도)을 60분법 각으로 입력하세요 : "))

# 지구의 평균 반지름
r = 6370.01

# 거리를 식에 맞게 계산한다.
distance = r * math.acos(math.sin(math.radians(x1)) * math.sin(math.radians(x2)) +
                         math.cos(math.radians(x1)) * math.cos(math.radians(x2)) *
                         math.cos(math.radians(y1) - math.radians(y2)))

# 결과를 출력한다.
print("두 점 사이의 거리는", distance, "km 입니다.")
