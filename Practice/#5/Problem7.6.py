#7.6

# QuadraticEquation 모듈의 QuadraticEquation 클래스 사용
from QuadraticEquation import QuadraticEquation

# 메인 함수
def main() :

    # a, b, c를 입력받는다.
    a, b, c = eval(input("a, b, c를 입력하세요 : "))

    # a, b, c를 가지고 객체를 만든다.
    q1 = QuadraticEquation(a, b, c)

    # 판별식이 0보다 크면
    if q1.getDiscriminant() > 0 :

        # 해를 2개 가진다.
        print(q1.getRoot1(), ",", q1.getRoot2())

    # 판별식이 0이면
    elif q1.getDiscriminant() == 0 :

        # 해를 1개 가진다.
        print(q1.getRoot1())

    # 판별식이 0보다 작으면
    else :

        # 해가 없다.
        print("이 방정식은 해가 없습니다.")


# 메인 함수 호출
main()    
