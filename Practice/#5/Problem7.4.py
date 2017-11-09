#7.4

# Fan 모듈의 Fan 클래스 사용
from Fan import Fan

# 메인 함수
def main() :

    # 객체1 : fan1
    fan1 = Fan()

    # 객체2 : fan2
    fan2 = Fan()

    # fan1의 속성 변경
    # 속도 = 가장 빠름
    # 색상 = 노랑
    # 전원 = 켜짐
    fan1.setSpeed(fan1.FAST)
    fan1.setRadius(10.0)
    fan1.setColor("Yellow")
    fan1.setOn(True)

    # fan2의 속성 변경
    # 속도 = 중간
    # 색상 = 파랑
    # 전원 = 꺼짐
    fan2.setSpeed(fan2.MEDIUM)
    fan2.setRadius(5.0)
    fan2.setColor("Blue")
    fan2.setOn(False)

    # 결과 출력
    print("**** 객체1 ****")
    print("속도 :", fan1.getSpeed())
    print("크기 :", fan1.getRadius())
    print("색상 :", fan1.getColor())
    print("전원 :", fan1.getOn())

    print()
    print()

    print("**** 객체2 ****")
    print("속도 :", fan2.getSpeed())
    print("크기 :", fan2.getRadius())
    print("색상 :", fan2.getColor())
    print("전원 :", fan2.getOn())


# 메인 함수 호
main()
