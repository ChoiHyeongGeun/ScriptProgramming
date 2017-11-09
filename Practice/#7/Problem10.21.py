#10.21 : 게임 (사물함 퍼즐)

# 사물함 퍼즐 함수
def puzzle() :

    # 사물함 리스트
    cabinet = []
    
    # 100번 반복
    for x in range(100) :

        # 사물함을 모두 닫는다.
        cabinet.append(False)

    # 1번 학생부터 100번 학생까지 반복
    for s in range(1, 101) :

        # 1번 학생이면
        if s == 1 :

            # 100번 반복
            for x in range(100) :

                # 모든 사물함을 연다.
                # x 인덱스의 내용을 삭제
                cabinet.pop(x)

                # x 인덱스에 True 삽입
                cabinet.insert(x, True)

        # 2번~100번 학생이면
        else :

            # 자기 번호의 배수들의 사물함의 상태를 반대로 바꾼다.
            # 100번 반복
            for x in range(1, 101) : 

                # 사물함 번호가 학생 번호로 나누어 떨어지면
                if x % s == 0 :

                    # 사물함이 열려있다면
                    if cabinet[x-1] == True :

                        # x 인덱스의 내용 삭제
                        cabinet.pop(x-1)

                        # x 인덱스에 False 삽입 (사물함을 닫는다.)
                        cabinet.insert(x-1, False)

                    # 사물함이 닫혀있다면
                    else :

                        # x 인덱스의 내용 삭제
                        cabinet.pop(x-1)

                        # x 인덱스에 True 삽입 (사물함을 연다.)
                        cabinet.insert(x-1, True)

    # 결과 출력
    print("<열려있는 사물함>")

    for i in range(100) :

        if cabinet[i] == True : 
            print("L", end='')
            print(i+1, end=', ')

# 메인 함수
def main() :

    # 사물함 퍼즐 시작
    puzzle()

# 메인 함수 호출
main()
