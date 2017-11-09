# 6.45

# turtle 모듈 사용
import turtle

# math 모듈 사용
import math

# n각형을 그리는 함수
def drawPolygon(x, y, radius, numberOfSides) :

    # turtle 모듈의 객체
    t = turtle.Turtle()

    # 선 굵기 = 5
    t.width(5)

    # n각형에서 한 각의 크기
    angle = 180 * (numberOfSides - 2) / numberOfSides

    # 각도로 변환
    radian = angle * math.pi / 180

    # 한 변의 크기
    side = 2 * radius / math.tan(radian / 2)

    # 이동선을 그리지 않는다.
    t.penup()

    # (x, y - radius)로 이동한다.
    t.goto(x, y - radius)

    # 이동선을 그린다.
    t.pendown()

    # 반지름이 radius인 원을 그린다.
    t.circle(radius)
    
    # 이동선을 그리지 않는다.
    t.penup()

    # (x, y + radius)로 이동한다.
    t.goto(x, y + side / (2 * math.cos(radian / 2)))

    # 이동선을 그린다.
    t.pendown()

    # 오른쪽으로 90 - angle / 2 만큼 꺾는다.
    t.right(90 - angle / 2)

    # 한 변의 길이만큼 그린다.
    t.forward(side)

    # n-1번 반복한다.
    for n in range(1, numberOfSides) :

        # 오른쪽으로 180 - angle 만큼 꺾는다.
        t.right(180 - angle)

        # 한 변의 길이만큼 그린다.
        t.forward(side)
        

drawPolygon(-250, 200, 50, 3) # 삼각형
drawPolygon(0, 200, 50, 4) # 사각형
drawPolygon(250, 200, 50, 5) # 오각형
drawPolygon(-250, -200, 50, 6) # 육각형
drawPolygon(0, -200, 50, 7) # 칠각형
drawPolygon(250, -200, 50, 8) # 팔각형
