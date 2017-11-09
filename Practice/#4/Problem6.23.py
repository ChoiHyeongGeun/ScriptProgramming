# 6.23

# 밀리초를 시:분:초 서식의 문자열로 반환하는 함수
def convertMillis(millis) :

    # 초 = 밀리초 / 1000
    second = (int)(millis / 1000)

    # 초가 60이상이면
    if second >= 60 :

        # 초를 분으로 바꾸고
        minute = (int)(second / 60)

        # 분으로 바꿨으므로 초에서 60 * 분을 뺀다.
        second = second - 60 * minute

    # 초가 60 미만이면
    else :

        # 시간과 분은 0이다.
        hour = minute = 0

    # 분이 60이상이면
    if minute >= 60 :

        # 분을 시간으로 바꾸고
        hour = (int)(minute / 60)

        # 시간으로 바꿨으므로 분에서 60 * 시간을 뺀다.
        minute = minute - 60 * hour

    # 분이 60 미만이면
    else :

        # 시간은 0이다
        hour = 0

    # 결과를 출력한다.
    print(hour, ":", minute, ":", second)

# 밀리초를 입력받는다.
millisecond = eval(input("밀리초를 입력하세요 : "))

# 결과를 출력한다.
convertMillis(millisecond)
