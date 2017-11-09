# 5.31

# 연도와 요일을 입력받는다.
year, day = eval(input("연도와 1월 1일의 요일을 입력하세요 (월요일=0 ~ 일요일=6): "))

# 12번 반복한다. (1월~12월)
for month in range(1, 13) :

    print() # 공백

    print() # 공백

    print("          ", year, "년", month, "월") # 해당연도 + 월

    print("----------------------------------")

    print(" 일   월   화   수   목   금   토 ")

    # 1월, 3월, 5월, 7월, 8월, 10월, 12월은
    if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12) :

        date = 31 # 31일까지 있다.

    # 4월, 6월, 9월, 11월은
    elif (month == 4) or (month == 6) or (month == 9) or (month == 11) :

        date = 30 # 30일까지 있다.

    # 2월은
    elif month == 2 :

        # 연도가 4로 나누어 떨어지지만
        # 100으로는 나누어 떨어지지 않고
        # 400으로는 나누어 떨어지면 윤년
        if (year % 4 == 0) and (year % 100 != 0) and (year % 400 == 0) :

            date = 29

        # 그렇지 않으면 평년
        else :

            date = 28


    # 요일마다 띄어서 출력시키기 위한 공백
    if day == 0 :
        
        print(end = '     ')
        
    elif day == 1 :
        
        print(end = '     ')
        print(end = '     ')
        
    elif day == 2 :
        
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        
    elif day == 3 :
        
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        
    elif day == 4 :
        
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        
    elif day == 5 :
        
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')
        print(end = '     ')

    # 날짜 출력 (1일 ~ )
    for cal in range(1, date + 1) :

        # 날짜 출력 + 공백
        print(format(cal, "3.0f"), end = '  ')

        # 현재 요일이 토요일이면
        if day == 5 :

            print() # 다음 줄로

        # 현재 요일이 일요일이면
        if day == 6 :

            # 요일 초기화
            day = -1

        day = day + 1
            
