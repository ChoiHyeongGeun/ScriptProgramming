# 8.8

# 2진수를 10진수로 변환
def binaryToDecimal(binaryString) :

    # 10진수
    decimal = 0

    # 2진수의 자릿수만큼 반복문 실행
    for x in range(0, len(binaryString)) :

        # 맨 앞자리부터 2^(자릿수-1)씩 곱해서 decimal에 저장한다.
        decimal = decimal + eval(binaryString[x]) * (2 ** (len(binaryString)-(x+1)))

    # 10진수 결과를 출력한다.
    print(decimal)

# 2진수를 입력받는다.
binaryString = input("2진수를 입력하세요 : ")

# binaryToDecimal을 호출한다.
binaryToDecimal(binaryString)
