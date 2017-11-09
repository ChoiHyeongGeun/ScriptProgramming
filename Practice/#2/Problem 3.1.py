# 3.1

# math 클래스를 import 한다.
import math

# 중심~꼭지점 길이를 직접 입력받는다.
r = eval(input("중심에서 꼭지점까지의 길이를 입력하세요 : "))

# 변의 길이(s)를 구한다.
s = 2 * r * math.sin(math.pi / 5)

# 넓이(w)를 구한다.
w = 3 * math.sqrt(3) / 2 * (s ** 2)

# 결과를 출력한다.
print("오각형의 넓이는", format(w, ".2f"), "입니다.")
