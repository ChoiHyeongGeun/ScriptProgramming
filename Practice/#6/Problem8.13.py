# 8.13

# 최장 공통 접두어
def prefix(s1, s2) :

    # 현재 단어
    word = ""

    # 현재까지 가장 긴 단어
    maxWord = ""

    # 인덱스
    x = 0

    # 단어 글자 수
    n = 2

    # 무한 루프
    while True :

        # x부터 x+n까지 반복문 실행
        for i in range(x, x+n) :

            # word에 s1[x]를 추가한다.
            word = word + s1[i]

        # word가 s2에 있다면
        if (word in s2) == True :

            # 현재까지 가장 긴 단어를 최신화한다.
            maxWord = word

        # 인덱스 1 증가
        x = x + 1

        # word 초기화
        word = ""

        # x+n이 s1의 글자수를 넘어간다면
        if (x+n) == len(s1)+1 :

            # 인덱스 초기화
            x = 0

            # 글자수 1 증가
            n = n + 1

        # 글자수가 s1의 글자수를 넘어간다면
        if n == len(s1)+1 :

            # 반복문 탈출
            break

    # 현재까지 가장 긴 단어 출력
    print(maxWord)
                
# s1과 s2를 입력받는다.
s1 = input("문자열1을 입력하세요 : ")
s2 = input("문자열2를 입력하세요 : ")

# prefix함수를 호출한다.
prefix(s1, s2)
