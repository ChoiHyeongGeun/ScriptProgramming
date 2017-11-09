# 4.11

# 년과 월을 입력받는다.
year, month = eval(input("년과 월을 입력하세요 : "))

# 1월, 3월, 5월, 7월, 8월, 10월, 12월 일 경우
if (month == 1) or (month == 3) or (month == 5) or (month == 7) or (month == 8) or (month == 10) or (month == 12) :
    # 31일까지 있다.
    day = 31
# 4월, 6월, 9월, 11월 일 경우
elif (month == 4) or (month == 6) or (month == 9) or (month == 11) :
    # 30일까지 있다.
    day = 30
# 2월 일 경우
elif month == 2 :
    # 연도가 4로 나누어 떨어진다면
    if year % 4 == 0 :
        # 윤년(29일)로 지정
        day = 29
        # 그런데 100으로도 나누어 떨어진다면
        if year % 100 == 0 :
            # 평년(28일)로 지정
            day = 28
            # 그렇지만 400으로 나누어 떨어진다면
            if year % 400 == 0 :
                # 다시 윤년(29일)로 지정
                day = 29
# 1월~12월에 해당하지 않는 경우
else :
    # 일단 일수를 0으로 지정
    day = 0

# 일수가 0이면
if day == 0 :
    # 에러 메시지를 준다.
    print("월을 잘못 입력하였습니다.")
# 일수가 0이 아니면
else :
    # 결과를 출력한다.
    print(year, "년", month, "월은", day, "일까지 있습니다.")
