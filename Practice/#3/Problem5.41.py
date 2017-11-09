# 5.41

# 루프 변수를 1로 초기화
i = 1

# 가장 큰 수를 0으로 초기화
max = 0

# 빈도수를 0으로 초기화
count = 0

# 무한 루프
while i > 0 :

    # 숫자를 입력받는다.
    number = eval(input("숫자를 입력하세요(0은 입력 종료) : "))

    # 입력받은 숫자가 0이면
    if number == 0 :

        # 무한 루프 탈출
        break

    # 입력받은 숫자가 현재 최대값보다 크면
    if number > max :

        # 최대값을 교체한다.
        max = number

        # 빈도수를 1로 변경한다.
        count = 1

    # 입력받은 숫자가 현재 최대값과 같다면
    elif number == max :

        # 빈도수만 1 증가시킨다.
        count = count + 1

# 루프문을 빠져나온 후에는 결과를 출력한다.
print("가장 큰 수는", max, "입니다.")
print("가장 큰 수가 나타난 빈도수는", count, "번입니다.")
