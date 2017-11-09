# 10.18 : 게임(8퀸)

# import 모듈 사용
import random

# 체스판의 각 행에 대한 리스트들
# 모든 요소들은 최초값으로 0을 갖는다.
chess0 = [0, 0, 0, 0, 0, 0, 0, 0]
chess1 = [0, 0, 0, 0, 0, 0, 0, 0]
chess2 = [0, 0, 0, 0, 0, 0, 0, 0]
chess3 = [0, 0, 0, 0, 0, 0, 0, 0]
chess4 = [0, 0, 0, 0, 0, 0, 0, 0]
chess5 = [0, 0, 0, 0, 0, 0, 0, 0]
chess6 = [0, 0, 0, 0, 0, 0, 0, 0]
chess7 = [0, 0, 0, 0, 0, 0, 0, 0]

# 행에 대한 리스트들의 모든 요소를 0으로 초기화
def reset() :

    # 8번 반복
    for i in range(8) :

        # 모든 요소들을 0으로 초기화
        change_chess(0, i, 0)
        change_chess(1, i, 0)
        change_chess(2, i, 0)
        change_chess(3, i, 0)
        change_chess(4, i, 0)
        change_chess(5, i, 0)
        change_chess(6, i, 0)
        change_chess(7, i, 0)

# 매개변수로 행과 열을 받아서 요소 반환
def return_chess(n, row) :

    # 입력받은 행에 따라서 그 행과 열의 내용을 반환
    if n == 0 : return chess0[row]
    elif n == 1 : return chess1[row]
    elif n == 2 : return chess2[row]
    elif n == 3 : return chess3[row]
    elif n == 4 : return chess4[row]
    elif n == 5 : return chess5[row]
    elif n == 6 : return chess6[row]
    elif n == 7 : return chess7[row]

# 매개변수로 행, 열을 받아서
# 행과 열에 해당하는 요소를 입력받은 값으로 변경
def change_chess(n, row, v) :

    # 입력받은 행에 따라서 그 행과 열의 내용을 입력받은 v로 변경
    if n == 0 :
        chess0.pop(row)
        chess0.insert(row, v)

    elif n == 1 :
        chess1.pop(row)
        chess1.insert(row, v)

    elif n == 2 :
        chess2.pop(row)
        chess2.insert(row, v)
        
    elif n == 3 :
        chess3.pop(row)
        chess3.insert(row, v)

    elif n == 4 :
        chess4.pop(row)
        chess4.insert(row, v)

    elif n == 5 :
        chess5.pop(row)
        chess5.insert(row, v)

    elif n == 6 :
        chess6.pop(row)
        chess6.insert(row, v)

    elif n == 7 :
        chess7.pop(row)
        chess7.insert(row, v)

# 같은 열에 Q를 두지 못하도록 요소를 1로 변경
def change_row(row) :

    # 8번 반복
    for i in range(8) :

        # 입력받은 열에 대해서 모든 행의 내용을 1로 변경
        change_chess(i, row, 1)

# 대각선에 Q를 두지 못하도록 요소를 1로 변경
def change_diagonal(line, row) :

    # 열+1 만큼 반복 (왼쪽 아래 대각선)
    for i in range(row+1) :

        # 내용을 1로 변경
        change_chess(line+i, row-i, 1)

        # 행 + i 가 7이 되면 반복문 탈출
        if line + i == 7 :

            break

    # 8-열 만큼 반복 (오른쪽 아래 대각선)
    for i in range(8-row) :

        # 내용을 1로 변경
        change_chess(line+i, row+i, 1)

        # 행 + i 가 7이 되면 반복문 탈출
        if line + i == 7 :

            break

# 다음 행에 대하여 Q를 둘 수 있는지 없는지 판단하는 함수
# (다음 행의 요소들이 모두 1이면 Q를 둘 수 없다.)
def can_Q(line) :

    # Q를 놓을 수 없는 자리의 수
    res = 0

    # 8번 반복
    for i in range(8) :

        # 하나의 행에 대한 모든 열을 검사하여
        # 1 (둘 수 없는 곳)이면 res를 1씩 증가
        if return_chess(line, i) == 1 :

            res = res + 1

    # 최종적으로 둘 수 있는 곳을 반환
    return 8 - res

# 체스판 결과를 출력하는 함수
def print_result() :

    # 8번 반복 (행)
    for x in range(8) :

        # 8번 반복 (열)
        for y in range(8) :

            # x행, y열의 내용을 n에 저장
            n = return_chess(x, y)

            # 작대기 출력
            print("|", end='')

            # 내용이 1이면 (Q를 둘 수 없는 곳)
            if n == 1 :

                print(" ", end='')

            # 내용이 9이면 (Q가 있는 곳)
            elif n == 9:

                print("Q", end='')

        # 작대기 출력
        print("|")

# 8퀸 게임 함수
def game() :

    # 초기화
    reset()

    # 행 = 0
    line = 0

    # 무한 반복
    while True :

        # 열 = 0~7 중에서 랜덤으로 생성
        row = random.randint(0, 7)

        # line행, row열의 내용이 0이면 (Q를 둘 수 있는 곳이면)
        if return_chess(line, row) == 0 :

            # row열 모두 Q를 못 두게 함
            change_row(row)

            # line, row의 대각선에 Q를 못 두게 함
            change_diagonal(line, row)

            # 현재 위치의 내용을 9로 바꿈
            change_chess(line, row, 9)

            # 다음 행에 Q를 둘 수 있는 곳이 0개이면
            if can_Q(line+1) == 0 :

                # 초기화
                reset()

                # 행 초기화
                line = 0

            # 다음 행에 Q를 둘 수 있으면
            else :

                # 행 + 1 하여 계속 진행
                line = line + 1

        # 행이 8이 되면 반복문 탈출
        if line == 8 :

            break

    # 결과 출
    print_result()

# 메인 함수
def main() :

    # 게임 시
    game()

# 메인 함수 호출
main()
