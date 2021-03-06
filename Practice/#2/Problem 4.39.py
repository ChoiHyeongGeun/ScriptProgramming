# 4.39

# math 모듈 사용
import math

# 첫 번째 원의 좌표와 반지름을 입력받는다.
x1, y1, r1 = eval(input("첫 번째 원의 좌표와 반지름을 입력하세요 : "))

# 두 번째 원의 좌표와 반지름을 입력받는다.
x2, y2, r2 = eval(input("두 번째 원의 좌표와 반지름을 입력하세요 : "))

# 두 원의 좌표 사이의 거리
distance = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))

# 좌표 사이의 거리가 두 원의 반지름의 합보다 크면
if (distance > r1 + r2) :
    # 두 원은 외부에 있으면서 겹치지 않는다.
    print("원2는 원1과 겹치지 않습니다.")
# 좌표 사이의 거리가 (원1의 반지름 - 원2의 반지름)과 같다면
elif (distance == r1 - r2) :
    # 원2는 원1에 속하면서 한 점에서 만난다.
    print("원2는 원1의 한 점에서 만납니다. (원2 ⊂ 원1)")
# 좌표 사이의 거리가 (원2의 반지름 - 원1의 반지름)과 같다면
elif (distance == r2 - r1) :
    # 원2는 원1을 포함하면서 한 점에서 만난다.
    print("원2는 원1의 한 점에서 만납니다. (원2 ⊃ 원1)")
# 좌표 사이의 거리가 (원1의 반지름 + 원2의 반지름)과 같다면
elif (distance == r1 + r2) :
    # 원2와 원1은 서로 바깥에 있으면서 한 점에서 만난다.
    print("원2는 원1의 한 점에서 만납니다. (원2 ≠ 원1)")
# 좌표 사이의 거리가 (원1의 반지름 + 원2의 반지름)보다 작으면서
elif (distance < r1 + r2) :
    # (원1의 반지름 - 원2의 반지름)보다 크다면
    if (distance > r1 - r2) :
        # 원2는 원1보다 작고 두 점에서 만난다.
        print("원2는 원1과 두 점에서 만납니다. (원2 < 원1)")
    # (원2의 반지름 - 원1의 반지름)보다 크다면
    elif (distance > r2 - r1) :
        # 원2는 원1보다 크고 두 점에서 만난다.
        print("원2는 원1과 두 점에서 만납니다. (원2 > 원1)")
