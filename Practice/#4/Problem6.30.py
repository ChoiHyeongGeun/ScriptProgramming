# 6.30

# random 모듈을 사용한다.
import random

# 주사위를 굴리는 함수
def craps() :

    # 주사위 1
    dice1 = random.randint(1, 6)

    # 주사위 2
    dice2 = random.randint(1, 6)

    # 두 주사위의 합을 반환
    return dice1 + dice2


# 주사위의 합이 4, 5, 6, 8, 9, 10일 경우
# 주사위를 다시 굴리는 함수
def recraps(n, c) :

    # 무한 루프
    while True :

        # 주사위를 굴린다.
        s = craps()

        # 이전 합과 새로운 합이 같으면
        if s == n :

            # 승리 횟수 1 증가 후 반환
            return c + 1

        # 새로운 합이 7이면
        elif s == 7 :

            # 패배 (승리 횟수 그대로 반환)
            return c


# 승패를 확인하는 함수
def result() :

    # 승리 횟수를 0으로 초기화
    count = 0

    # 10000번 반복
    for x in range(0, 10000) :

        # 주사위를 굴린다.
        sum = craps()

        # 합이 7 또는 11이면
        if (sum == 7) or (sum == 11) :

            # 승리 횟수 1 증가
            count = count + 1

        # 합이 2 또는 3 또는 12이면
        elif (sum == 2) or (sum == 3) or (sum == 12) :

            # 승리 횟수 0 증가
            count = count

        # 합이 그 이외의 값이면
        else :

            # 주사위를 다시 돌린다.
            count = recraps(sum, count)

    # 승리 횟수를 출력한다.
    print("승리 횟수 :", count)


# 게임 시작
result()
