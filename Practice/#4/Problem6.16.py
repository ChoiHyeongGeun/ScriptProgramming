# 6.16

# 1년의 총 일수를 구하는 함
def numberOfDaysInYear(year) :

    # 윤년이면
    if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0) :

        return 366 # 총 366일

    # 윤년이 아니면
    else :

        return 365 # 총 365일

    
# 결과를 출력하는 함수
def printResult() :

    # 일수의 총 합을 0으로 초기화
    sum = 0

    # 2010년부터 2020년까지
    for x in range(2010, 2021) :

        # 총 일수를 합한다.
        sum = sum + numberOfDaysInYear(x)

    # 그 결과를 출력한다.
    print("2010년부터 2020년까지의 총 일수는", sum, "일 입니다.")


# 메인에서 결과를 출력한다.
printResult()
