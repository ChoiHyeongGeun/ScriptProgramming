# 11.6 - 대수학 : 행렬의 곱

# math 모듈 사용
import math

# 결과를 출력하는 함수
def printResult(a, b, c, size) :

    for i in range(size) :

        # A행렬 출력
        for j in range(size) :

            print(format(a[i][j], "2.1f"), end=' ')

        # 곱셈 부호 붙이기
        if i == (int)(size/2) :

            print("   *   ", end='')

        else :

            print("       ", end='')

        # B행렬 출력
        for j in range(size) :

            print(format(b[i][j], "2.1f"), end=' ')

        # = 부호 붙이기
        if i == (int)(size/2) :

            print("   =   ", end='')

        else :

            print("       ", end='')

        # C행렬 출력
        for j in range(size) :

            print(format(c[i][j], "2.1f"), end=' ')

        print()

# 두 행렬을 곱하는 함수
def multiplyMatrix(a, b) :

    lstA = [] # A행렬의 1차원 리스트 (행)
    matA = [] # A행렬의 2차원 리스트

    lstB = [] # B행렬의 1차원 리스트 (행)
    matB = [] # B행렬의 2차원 리스트

    lstC = [] # C행렬의 1차원 리스트 (행)
    matC = [] # C행렬의 2차원 리스트

    # size = 행 또는 열의 크기
    size = (int)(math.sqrt(len(a)))

    # a, b (1차원 리스트)를 A, B (2차원 리스트)로 변환
    for i in range(len(a)) :

        lstA.append(a[i])
        lstB.append(b[i])

        if (i+1) % size == 0 :

            matA.append(lstA)
            matB.append(lstB)
            
            lstA = []
            lstB = []

    # s = 행렬의 곱셈
    s = 0

    # 행렬의 곱셈 (3중 반복문)
    for x in range(size) :

        for y in range(size) :

            for z in range(size) :

                # s에 행렬의 곱셈값을 넣는다.
                s = s + matA[x][z] * matB[z][y]

            # 곱한 값을 lstC행렬에 추가하고, s를 초기화 시킨다.
            lstC.append(s)
            s = 0

        # 한 행의 곱셈이 모두 끝나면 lstC를 matC에 추가한다.
        # lstC를 초기화 시킨다.
        matC.append(lstC)
        lstC = []

    # 결과를 출력한다.
    printResult(matA, matB, matC, size)

# 메인 함수
def main() :

    # 행렬1과 행렬2를 입력받는다.
    # 입력받은 행렬을 2차원 리스트로 저장한다.
    m = input("행렬1을 입력하세요 : ")
    lst = m.split()
    a = [eval(x) for x in lst]

    m = input("행렬2를 입력하세요 : ")
    lst = m.split()
    b = [eval(x) for x in lst]

    # 모든 요소의 개수의 루트값이 정수값이면 함수 실행
    # n x n 행렬 이면 함수 실행
    if math.sqrt(len(a)) == (int)(math.sqrt(len(a))) :

        multiplyMatrix(a, b)

    # n x n 행렬이 아니면 에러메시지
    else :

        print("행렬을 잘못 입력하였습니다.")

# 메인 함수 호출
main()
