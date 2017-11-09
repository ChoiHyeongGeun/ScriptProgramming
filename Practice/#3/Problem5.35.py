# 5.35

# 2부터 10000까지 반복한다.
for x in range(2, 10000) :

    # 약수들의 합을 0으로 초기화한다.
    sum = 0

    # 1부터 x-1까지 반복한다.
    for y in range(1, x) :

        # x가 y로 나누어 떨어진다면 그것은 약수이다.
        if x % y == 0 :

            # 약수를 합한다.
            sum = sum + y

    # 약수들의 합이 x와 같으면 완전수이다.
    if sum == x :

        print(x) # 결과 출력