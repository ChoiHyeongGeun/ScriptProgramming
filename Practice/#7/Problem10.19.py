# 10.19 : 게임(콩 기계)

import random

# 콩이 왼쪽으로 갈건지 오른쪽으로 갈건지 정하는 함수
def leftOrRight() :

    # 0과 1 중 랜덤으로 하나 선택
    n = random.randint(0, 1)

    # 0이면 True 반환
    if n == 0 :

        return True

    # 1이면 False 반환
    else :

        return False

# 콩들의 결과를 보여주는 함수
def printResult(b, s, result) :

    # m : 가장 많은 콩 수
    m = 0

    # 각 슬롯에 있는 콩의 개수들의 리스트
    num = []

    # 슬롯의 개수만큼 반복
    for x in range(s) :

        # result 리스트에 있는 x의 개수를 반환
        n = result.count(x)

        # 개수를 num 리스트에 저장
        num.append(n)

        # 가장 많은 콩 수보다 n이 많으면
        if m < n :

            # 가장 많은 콩 수 최신화
            m = n

    # 결과를 출력할 리스트
    lst = [" ", " ", " ", " ", " ", " ", " ", " "]

    # 가장 많은 콩 수만큼 반복
    for x in range(m, 0, -1) :

        # 결과를 출력할 리스트
        r = [] + lst

        # 슬롯의 개수만큼 반복
        for y in range(s) :

            # 콩의 개수가 x와 같으면
            if num[y] == x :

                # r 리스트의 y 인덱스에 있는 내용을 삭제 (빈칸 삭제)
                r.pop(y)

                # r 리스트의 y 인덱스에 0을 삽입
                r.insert(y, "0")

                # n1 = 원래 콩의 개수
                n1 = num[y]

                # n2 = 원래 콩의 개수 - 1
                n2 = num[y] - 1

                # num 리스트의 y 인덱스에 있는 내용을 삭제 (원래 콩의 개수)
                num.pop(y)

                # num 리스트의 y 인덱스에 n2를 삽입 (최신화된 콩의 개수)
                num.insert(y, n2)

            # 결과 한 줄 출력
            print(r[y], end='')

        # 줄바꿈
        print()
        
# 게임 함수
def game(b, s) :

    # 콩의 경로를 저장하는 리스트
    list1 = []

    # 콩들이 움직인 거리를 저장하는 리스트 (왼쪽 : -1, 오른쪽 : +1)
    save = [] 

    # 콩들의 최종 위치들을 저장하는 리스트
    result = []

    # 콩의 개수만큼 반복
    for x in range(b) :

        # list1 초기화
        list1 = []

        # pos : 콩의 현재 위치
        pos = 0

        # 슬롯의 개수-1 만큼 반복
        for y in range(s-1) :

            # leftOrRight 호출
            go = leftOrRight()

            # go 가 True이면 왼쪽
            if go == True :

                # list1 리스트에 L 삽입
                list1.append("L")

                # 현재 위치 = 현재 위치 - 1
                pos = pos - 1

            # go 가 False이면 오른쪽
            else :

                # list1 리스트에 R 삽입
                list1.append("R")

                # 현재 위치 = 현재 위치 + 1
                pos = pos + 1

            # list1의 내용 호출
            print(list1[y], end='')

        # 띄어쓰기
        print()

        # 콩이 총 움직인 거리를 save 리스트에 저장
        save.append(pos)

        # 슬롯의 개수만큼 반복
        for y in range(s) :

            # 콩이 총 움직인 거리를 슬롯 번호로 바꾸는 과정
            if save[x] == (-(s-1) + 2 * y) :

                # result 리스트에 y 삽입
                result.append(y)

    # 결과 출력
    printResult(b, s, result)

# 메인 함수
def main() :

    # 콩의 개수와 슬롯의 개수를 입력받는다.
    b = eval(input("떨어뜨릴 공의 개수를 입력하세요 : "))
    s = eval(input("콩 기계의 슬롯 개수를 입력하세요 : "))

    # 게임 시작
    game(b, s)

# 메인 함수 호출
main()
