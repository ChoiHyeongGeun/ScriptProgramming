# 2.18 : 현재 시간

import time

# 현재 시간을 얻어온다.
currentTime = time.time()

# GMT와 시간대 차이를 직접 입력받는다.
timeGap = eval(input("GMT와 시간대 차이를 입력하세요 : "))

# 1970년 1월 1일 자정 이후로의 전체 초 값을 얻어온다.
totalSeconds = int(currentTime)

# 현재시간의 초 값을 계산한다.
currentSecond = totalSeconds % 60

# 전체 분 값을 계산한다.
totalMinutes = totalSeconds // 60

# 현재 시간의 분 값을 계산한다.
currentMinute = totalMinutes % 60

# 전체 시 값을 계산한다.
totalHours = totalMinutes // 60

# 현재 시간의 시 값을 계산한다.
currentHour = (totalHours % 24) + timeGap

# 결과를 출력한다.
print("현재 시간은" + str(currentHour) + ":"
      + str(currentMinute) + ":" + str(currentSecond) + "GMT")
