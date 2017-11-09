# 6.3

# reverse 함수를 정의하고 매개변수로 number를 받는다.
def reverse(number) :

    # 1의 자리 숫자를 추출한다.
    num1 = number % 10

    # 10의 자리 숫자를 추출한다.
    num10 = ((number - num1) / 10) % 10

    # 100의 자리 숫자를 추출한다.
    num100 = ((number - num1 - num10 * 10) / 100) % 10

    # 숫자를 뒤집어서 newNumber에 저장한다.
    newNumber = num100 + (num10 * 10) + (num1 * 100)

    # newNumber를 반환한다.
    return int(newNumber)


# isPalindrome 함수를 정의하고 매개변수로 number를 받는다.
def isPalindrome(number) :

    # number를 뒤집은 후 reverseNumber에 저장한다.
    reverseNumber = reverse(number)

    # 뒤집어도 값이 같다면
    if number == reverseNumber :

        # True를 반환한다.
        return True

    # 뒤집어서 값이 다르면
    else :

        # False를 반환한다.
        return False


# 숫자를 입력받는다.
num = eval(input("숫자를 입력하세요 : "))

# True를 반환했다면
if isPalindrome(num) == True :

    # 대칭수이다.
    print("입력한 숫자는 대칭수 입니다.")

# False를 반환했다면
else :

    # 대칭수가 아니다.
    print("입력한 숫자는 대칭수가 아닙니다.")
