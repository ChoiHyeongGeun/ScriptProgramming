# 6.10

# isPrime 함수를 정의하고 매개변수로 number를 받는다.
def isPrime(number) :

    # 결과 출력 시 줄바꿈을 위한 카운트
    lineChange = 0

    # 만약 매개변수가 2이면
    if number == 2 :

        # 2는 소수이므로 2를 출력하고
        print("2")

        # 함수를 끝낸다.
        return

    # 1부터 number-1까지 반복한다.
    for x in range(1, number) :

        # 약수의 개수를 0으로 초기화한다.
        count = 0

        # 1부터 x까지 반복한다.
        for y in range(1, x) :

            # 딱 나누어 떨어지면 약수이므로
            if x % y == 0 :

                # 약수의 개수를 증가시킨다.
                count = count + 1

        # 만약 약수의 개수가 1개이면
        if count == 1 :

            # 소수이므로 결과를 출력한다.
            print(format(x, "5.0f"), end = '  ')

            # 줄바꿈 카운트를 증가시킨다.
            lineChange = lineChange + 1

            # 줄바꿈 카운트가 10이면
            if lineChange == 10 :

                # 줄바꿈 카운트를 초기화시키고
                lineChange = 0

                # 줄을 바꾼다.
                print()


# 숫자를 입력받는다.
num = eval(input("숫자를 입력하세요 : "))

print(num, "이하의 숫자 중에서 소수를 찾습니다.")

# 소수를 찾는다.
isPrime(num)
