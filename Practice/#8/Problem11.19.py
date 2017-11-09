# 11.19 - 패턴 인식 : 네 개의 연속된 같은 숫자

# a 와 b 와 c 와 d 가 같은지 판단하는 함수
def isEqual(a, b, c, d) :

    # a == b == c == d이면 True를 반환
    if (a == b) and (b == c) and (c == d) :

        return True

    # 아니면 False를 반환
    else :

        return False

# 가로로 연속된 4개의 숫자가 있는지 판단하는 함수
def isWidth(v) :

    # 검사할 행의 범위 : 0 ~ 행의수
    for x in range(0, len(v)) :

        # 검사할 열의 범위 : 0 ~ 열의수-3
        for y in range(0, len(v[0])-3) :

            # 가로로 연속된 4개의 숫자가 같은 값이면 True 반환
            if isEqual(v[x][y], v[x][y+1], v[x][y+2], v[x][y+3]) == True :

                return True

    # 아니면 False 반환
    return False

# 세로로 연속된 4개의 숫자가 있는지 판단하는 함수
def isHeight(v) :

    # 검사할 행의 범위 : 0 ~ 행의수-3
    for x in range(0, len(v)-3) :

        # 검사할 열의 범위 : 0 ~ 열의수
        for y in range(0, len(v[0])) :

            # 세로로 연속된 4개의 숫자가 같은 값이면 True 반환
            if isEqual(v[x][y], v[x+1][y], v[x+2][y], v[x+3][y]) == True :

                return True

    # 아니면 False 반환
    return False

# / 대각선으로 연속된 4개의 숫자가 있는지 판단하는 함수
def isLeftDiagonal(v) :

    # 검사할 행의 범위 : 0 ~ 행의수-3
    for x in range(0, len(v)-3) :

        # 검사할 열의 범위 : 3 ~ 열의수
        for y in range(3, len(v[0])) :

            # / 대각선으로 연속된 4개의 숫자가 같은 값이면 True 반환
            if isEqual(v[x][y], v[x+1][y-1], v[x+2][y-2], v[x+3][y-3]) == True :

                return True

    # 아니면 False 반환
    return False

# ＼ 대각선으로 연속된 4개의 숫자가 있는지 판단하는 함수
def isRightDiagonal(v) :

    # 검사할 행의 범위 : 0 ~ 행의수-3
    for x in range(0, len(v)-3) :

        # 검사할 열의 범위 : 0 ~ 열의수-3
        for y in range(0, len(v[0])-3) :

            # ＼ 대각선으로 연속된 4개의 숫자가 같은 값이면 False 반환
            if isEqual(v[x][y], v[x+1][y+1], v[x+2][y+2], v[x+3][y+3]) == True :

                return True

    # 아니면 False 반환
    return False

# 연속된 4개의 숫자가 있는지 판단하는 함수 + 결과 출력
def isConsecutiveFour(v) :

    # 입력받은 행렬 출력
    for x in range(len(v)) :

        print(v[x])

    # 4가지 경우를 검사하여 해당되면 True 출력
    if isWidth(v) == True :

        print("True : → 가로")

    elif isHeight(v) == True :

        print("True : ↓ 세로")

    elif isLeftDiagonal(v) == True :

        print("True : ↙ 대각선")

    elif isRightDiagonal(v) == True :

        print("True : ↘ 대각선")

    # 4가지 경우에 모두 해당하지 않으면 False 출력
    else :

        print("False")

# 메인 함수
def main() :

    # 행과 열의 개수를 입력받는다.
    line = eval(input("행의 개수를 입력하세요 : "))
    row = eval(input("열의 개수를 입력하세요 : "))

    # 행렬의 내용을 입력받는다. (1차원 리스트)
    s = input("리스트의 값들을 입력하세요 : ")
    items = s.split()

    lst = [] # 1차원 리스트
    values = [] # 2차원 리스트

    # items의 내용을 values에 2차원 리스트로 저장한다.
    for i in range(len(items)) :

        # items의 내용을 정수값으로 lst에 저장한다.
        lst.append(eval(items[i]))

        # i+1이 열의 수의 배수가 되면
        if (i+1) % row == 0 :

            # values에 lst를 추가하고 lst를 초기화한다.
            values.append(lst)
            lst = []

    # items의 개수와 행의수 x 열의수와 다르면 에러메시지
    if len(items) != (line * row) :

        print("잘못 입력하였습니다.")

    # 같다면 함수 호출
    else :

        isConsecutiveFour(values)

# 메인 함수 호출
main()
