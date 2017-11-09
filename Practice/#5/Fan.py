# Fan 클래스
    
class Fan :

    # SLOW = 1, MEDIUM = 2, FAST = 3
    SLOW = 1
    MEDIUM = 2
    FAST = 3

    # 생성자
    def __init__(self, speed = SLOW, radius = 5.0, color = "Blue", on = False) :

        # private int 데이터필드 : 팬의 속도
        self.__speed = speed

        # private float 데이터필드 : 팬의 반지름
        self.__radius = radius

        # private String 데이터필드 : 팬의 색상
        self.__color = color

        # private bool 데이터필드 : 팬의 작동 여부
        self.__on = on

    # 팬의 속도를 설정하는 함수
    def setSpeed(self, s) :

        self.__speed = s

    # 팬의 속도를 반환하는 함수
    def getSpeed(self) :

        return self.__speed

    # 팬의 작동 여부를 설정하는 함수
    def setOn(self, o) :

        self.__on = o

    # 팬의 작동 여부를 반환하는 함수
    def getOn(self) :

        return self.__on

    # 팬의 반지름을 설정하는 함수
    def setRadius(self, r) :

        self.__radius = r

    # 팬의 반지름을 반환하는 함수
    def getRadius(self) :

        return self.__radius

    # 팬의 색상을 설정하는 함수
    def setColor(self, c) :

        self.__color = c

    # 팬의 색상을 반환하는 함수
    def getColor(self) :

        return self.__color
