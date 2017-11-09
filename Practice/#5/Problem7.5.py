# 7.5

# RegularPolygon 모듈의 RegularPolygon 클래스 사용
from RegularPolygon import RegularPolygon

# 메인 함수
def main() :

    # 객체 1
    r1 = RegularPolygon()

    # 객체 2
    r2 = RegularPolygon(6, 4)

    # 객체 3
    r3 = RegularPolygon(10, 4, 5.6, 7.8)

    # 결과 출력
    print("**** 객체1 ****")
    print("둘레 :", r1.getPerimeter())
    print("넓이 :", r1.getArea())

    print()
    print()
    
    print("**** 객체2 ****")
    print("둘레 :", r2.getPerimeter())
    print("넓이 :", r2.getArea())

    print()
    print()
    
    print("**** 객체3 ****")
    print("둘레 :", r3.getPerimeter())
    print("넓이 :", r3.getArea())


# 메인 함수 출
main()
