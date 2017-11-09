# 4.8

# 정수 3개를 입력받는다.
a, b, c = eval(input("정수 3개를 입력하세요 : "))

# 만약 a가 b보다 크거나 같을 때
if a >= b :
    # a가 c보다 크거나 같으면
    if a >= c :
        # a가 가장 큰 수
        num3 = a
        # b가 c보다 크거나 같으면
        if b >= c :
            # b가 두 번째로 큰 수
            num2 = b
            # c가 가장 작은 수
            num1 = c
        # c가 b보다 크면
        else :
            # c가 두 번째로 큰 수
            num2 = c
            # b가 가장 작은 수
            num1 = b
    # c가 a보다 크면
    else :
        # c가 가장 큰 수
        num3 = c
        # a가 두 번째로 큰 수
        num2 = a
        # b가 가장 작은 수
        num1 = b
# 만약 b가 a보다 클 때
else :
    # b가 c보다 크거나 같으면
    if b >= c :
        # b가 가장 큰 수
        num3 = b
        # c가 a보다 크거나 같으면
        if c >= a :
            # c가 두 번째로 큰 수
            num2 = c
            # a가 가장 작은 수
            num1 = a
        # a가 c보다 크면
        else :
            # a가 두 번째로 큰 수
            num2 = a
            # c가 가장 작은 수
            num1 = c
    # c가 b보다 크면
    else :
        # c가 가장 큰 수
        num3 = c
        # b가 두 번째로 큰 수
        num2 = b
        # a가 가장 작은 수
        num1 = a

# 결과를 출력한다.
print(num1, ",", num2, ",", num3)
