#7.7

# LinearEquation 모듈의 LinearEquation 클래스 사용
from LinearEquation import LinearEquation

# 메인 함수
def main() :

    # a, b, c, d, e, f를 입력받는다.
    a, b, c, d, e, f = eval(input("a, b, c, d, e, f를 입력하세요 : "))

    # 객체 생성
    l1 = LinearEquation(a, b, c, d, e, f)

    # ad-bc가 0이 아니면
    if l1.isSolvable() == True :

        # x와 y를 출력
        print("x =", l1.getX(), ", y =", l1.getY())

    # ad-bc가 0이면
    else :

        # 해가 없다고 출력
        print("이 방정식은 해가 없습니다.")


# 메인 함수 호출
main()
