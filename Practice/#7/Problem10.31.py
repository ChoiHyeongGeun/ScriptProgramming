# 10.31 : 문자열 내 각 숫자의 빈도수

# 문자열 내 각 숫자의 빈도수를 구하는 함수
def count(s) :

    # 문자열을 저장할 리스트
    lst = []

    # 문자열의 개수만큼 반복
    for x in range(len(s)) :

        # 해당 글자가 숫자이면
        if s[x].isdigit() == True : 

            # 숫자로 변경하여 lst에 삽입
            lst.append(eval(s[x]))

    # 빈도수를 저장할 리스트
    result = []

    # 10번 반복
    for x in range(10) :

        # x의 빈도수를 구해서 result 리스트에 저장
        result.append(lst.count(x))

    # result 리스트 반환
    return result

# 메인 함수
def main() :

    # 문자열을 입력받아서 count 함수 호출
    counts = count(input("문자열을 입력하세요 : "))

    # 10번 반복
    for x in range(10) :

        # 빈도수가 0이 아니면
        if counts[x] != 0 : 

            # 결과 출력
            print(x, "-", counts[x], "번 나타납니다.")

# 메인 함수 호출
main()
