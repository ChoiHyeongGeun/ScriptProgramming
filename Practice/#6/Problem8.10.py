# 8.10

# 10진수를 2진수로 변환
def decimalToBinary(value) :

    # 입력받은 값을 복사
    binaryValue = value

    # 인덱스
    x = 0

    # 무한 루프
    while True :

        # binaryValue가 2^x을 넘지 않으면
        if binaryValue < (2 ** x) :

            # 반복문 탈출
            break

        # binaryValue가 2^x을 넘으면
        # x를 1 증가한다.
        x = x + 1

    # 2^x가 binaryValue를 넘어간 상태이므로
    # x를 1 감소시켜서 2^x가 binaryValue보다 작은 최대 2^x로 만든다.
    x = x - 1

    # 무한 루프
    while True : 

        # binaryValue가 2^x보다 크면
        if binaryValue >= (2 ** x) :

            # binaryValue에서 2^x값을 빼고
            binaryValue = binaryValue - (2 ** x)

            # 1을 출력한다.
            print("1", end='')

        # binaryValue가 2^x보다 작으면
        else :

            # 0을 출력한다.
            print("0", end='')

        # x를 1 감소한다.
        x = x - 1

        # x가 음수이면
        if x < 0 :

            # 반복문 탈출
            break

# 10진수를 입력받는다.
value = eval(input("10진수를 입력하세요 : "))

# decimalToBinary를 호출한다.
decimalToBinary(value)
