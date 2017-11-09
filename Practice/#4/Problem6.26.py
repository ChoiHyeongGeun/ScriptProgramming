# 6.26

# n이 소수인지 아닌지 판별하는 함수
def isPrime(n) :

    # n이 1 이하면
    if n <= 1 :

        # 소수가 아니다.
        return False

    # n이 2이면
    elif n == 2 :

        # 소수다.
        return True

    # n이 3 이상이면
    elif n >= 3 :

        # 2부터 n-1까지
        for x in range(2, n) :

            # n과 나누어지는게 있으면
            if n % x == 0 :

                # 소수가 아니다.
                return False

        # 나누어지는게 없으면 소수다.
        return True


# 메르센 소수를 찾는 함수
def mersennePrime(x) :

    # 2부터 x까지
    for p in range(2, x+1) :

        # 2^p - 1이 소수이면
        if isPrime((2 ** p) - 1) == True :

            # 메르센소수이므로 출력한다.
            print(format(p, "3.0f"), format((2 ** p) - 1, "10.0f"))


# 메르센 소수를 찾는다.
mersennePrime(31)
