# 4.1

# math 모듈 사용
import math

# a, b, c 를 입력받는다.
a, b, c = eval(input("a, b, c를 입력하세요 : "))

# 판별식을 d에 저장한다.
d = b*b - 4*a*c

# 만약 판별식이 양수이면
if d > 0 :
    # 첫 번째 실근을 구한다.
    r1 = (-b + math.sqrt(d)) / 2*a
    # 두 번째 실근을 구한다.
    r2 = (-b - math.sqrt(d)) / 2*a
    # 두 실근을 출력한다.
    print("실근은", format(r1, ".6f"), "이고", format(r2, ".6f"), "입니다.")
# 만약 판별식이 0이면
elif d == 0 :
    # 하나의 실근을 구한다.
    r1 = -b / 2*a
    # 실근을 출력한다.
    print("실근은", r1, "입니다.")
# 만약 판별식이 음수이면
else :
    # 실근이 존재하지 않다고 출력한다.
    print("이 방정식은 실근이 존재하지 않습니다.")