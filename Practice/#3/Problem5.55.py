# 5.55

# turtle 모듈 사용
import turtle

# 하얀색 사각형을 그리는 함수
def White() :

    # 4번 반복한다.
    for x in range(4) :

        # 정면으로 100만큼 그리고
        turtle.forward(100)

        # 왼쪽으로 90도 꺾는다.
        turtle.left(90)


# 검은색 사각형을 그리는 함수
def Black() :

    # 색 채우기를 시작한다.
    turtle.begin_fill()

    # 4번 반복한다.
    for x in range(4) :

        # 정면으로 100만큼 그리고
        turtle.forward(100)

        # 왼쪽으로 90도 꺾는다.
        turtle.left(90)

    # 검은색으로 칠한다.
    turtle.fillcolor("black")

    # 색 채우기를 종료한다.
    turtle.end_fill()


# x, y 좌표로부터 한 줄을 검은색 사각형부터 그리는 함수
def DrawBlack(x, y) :

    # 무한 루프
    while(True) :

        # x, y 좌표로 이동한다.
        turtle.goto(x, y)

        # 200으로 나누어지면
        if x % 200 == 0 :

            # 검은색 사각형을 그린다.
            Black()

        # 200으로 나누어지지 않으면
        else :

            # 하얀색 사각형을 그린다.
            White()

        # x 좌표가 300에 도달하면
        if x == 300 :

            # 무한 루프를 빠져나온다.
            break

        # x의 좌표를 100만큼 이동시킨다.
        x = x + 100

    # x, y 좌표로 이동한다.
    turtle.goto(x, y)

    # y 좌표를 100만큼 이동시킨다.
    turtle.goto(x, y+100)


# x, y 좌표로부터 한 줄을 하얀색 사각형부터 그리는 함수
def DrawWhite(x, y) :

    # 무한 루프
    while(True) :

        # x, y 좌표로 이동한다.
        turtle.goto(x, y)

        # 200으로 나누어지면
        if x % 200 == 0 :

            # 하얀색 사각형을 그린다.
            White()

        # 200으로 나누어지지 않으면
        else :

            # 검은색 사각형을 그린다.
            Black()

        # x 좌표가 300에 도달하면
        if x == 300 :

            # 무한 루프를 빠져나온다.
            break

        # x의 좌표를 100만큼 이동시킨다.
        x = x + 100

    # x, y 좌표로 이동한다.
    turtle.goto(x, y)

    # y의 좌표를 100만큼 이동시킨다.
    turtle.goto(x, y+100)


# 체스판을 그리는 함수
def Chess() :

    # 선 굵기를 5로 정한다.
    turtle.width(5)

    # 선을 그리는 속도를 최대로 높인다.
    turtle.speed('fastest')

    # (0, -400)으로 이동한다.
    turtle.goto(0, -400)

    # (-400, -400)으로 이동하여 검은색 사각형부터 그린다.
    DrawBlack(-400, -400)

    # (-400, -300)으로 이동하여 하얀색 사각형부터 그린다.
    DrawWhite(-400, -300)

    # (-400, -200)으로 이동하여 검은색 사각형부터 그린다.
    DrawBlack(-400, -200)

    # (-400, -100)으로 이동하여 하얀색 사각형부터 그린다.
    DrawWhite(-400, -100)

    # (-400, 0)으로 이동하여 검은색 사각형부터 그린다.
    DrawBlack(-400, 0)

    # (-400, 100)으로 이동하여 하얀색 사각형부터 그린다.
    DrawWhite(-400, 100)

    # (-400, 200)으로 이동하여 검은색 사각형부터 그린다.
    DrawBlack(-400, 200)

    # (-400, 300)으로 이동하여 하얀색 사각형부터 그린다.
    DrawWhite(-400, 300)

    

Chess() # 체스판을 그린다.
