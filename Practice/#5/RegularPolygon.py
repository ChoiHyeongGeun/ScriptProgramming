# math 모듈 사용
import math

# RegularPolygon 클래스
class RegularPolygon :

    # 생성자
    def __init__(self, n = 3, side = 1.0, x = 0.0, y = 0.0) :

        # private int 데이터필드 : 다각형 변의 개수
        self.__n = n

        # private float 데이터필드 : 변의 길이
        self.__side = side

        # private float 데이터필드 : x 좌표
        self.__x = x

        # private float 데이터필드 : y 좌표
        self.__y = y

    # 변의 개수를 설정하는 함수
    def setN(self, n) :

        self.__n = n

    # 변의 개수를 반환하는 함수
    def getN(self) :

        return self.__n

    # 변의 길이를 설정하는 함수
    def setSide(self, s) :

        self.__side = s

    # 변의 길이를 반환하는 함수
    def getSide(self) :

        return self.__side

    # x 좌표를 설정하는 함수
    def setX(self, x) :

        self.__x = x

    # x 좌표를 반환하는 함수
    def getX(self) :

        return self.__x

    # y 좌표를 설정하는 함수
    def setY(self, y) :

        self.__y = y

    # y 좌표를 반환하는 함수
    def getY(self) :

        return self.__y

    # 다각형의 둘레를 반환하는 함수
    def getPerimeter(self) :

        return self.__side * self.__n

    # 다각형의 넓이를 반환하는 함
    def getArea(self) :

        return (self.__n * math.pow(self.__side, 2)) / (4 * math.tan(math.pi / self.__n))
