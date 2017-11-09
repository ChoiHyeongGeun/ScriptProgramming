# 8.3

# 패스워드 검사하기
def password() :

    # 패스워드를 입력받는다.
    pw = input("패스워드를 입력하세요 : ")

    # 문자 개수
    alphaCount = 0

    # 1. 패스워드가 최소한 8개의 문자를 가지지 않다면 올바르지 않은 패스워드이다.
    for x in range(0, len(pw)) :

        # 글자 하나 하나 검사해서 문자이면
        if pw[x].isalpha() == True :

            # 문자 개수 + 1
            alphaCount = alphaCount + 1

    # 문자 개수가 8개 미만이면
    if alphaCount < 8 :

        # 올바르지 않은 패스워드
        print("올바르지 않은 패스워드입니다.")

        return

    # 2. 패스워드가 문자와 숫자로만 이루어져있지 않다면 올바르지 않은 패스워드이다.
    if pw.isalnum() == False :

        print("올바르지 않은 패스워드 입니다.")

        return

    # 숫자 개수
    numCount = 0

    # 3. 패스워드가 최소한 두 개의 숫자를 가지지 않다면 올바르지 않은 패스워드이다.
    for x in range(0, len(pw)) :

        # 글자 하나 하나 검사하여 숫자이면
        if pw[x].isdigit() == True :

            # 숫자 개수 + 1
            numCount = numCount + 1

    # 숫자 개수가 2개 미만이면
    if numCount < 2 :

        # 올바르지 않은 패스워
        print("올바르지 않은 패스워드입니다.")

        return


    # 1, 2, 3 모두 해당하지 않다면 올바른 패스워드이다.
    print("올바른 패스워드입니다.")

# password를 호출한다.
password()
