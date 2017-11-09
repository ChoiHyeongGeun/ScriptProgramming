# LinearEquation 클래스
class LinearEquation :

    # 생성자
    def __init__(self, a = 0, b = 0, c = 0, d = 0, e = 0, f = 0) :

        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    # a를 반환하는 함수
    def getA(self) :

        return self.__a

    # b를 반환하는 함수
    def getB(self) :

        return self.__b

    # c를 반환하는 함수
    def getC(self) :

        return self.__c

    # d를 반환하는 함수
    def getD(self) :

        return self.__d

    # e를 반환하는 함수
    def getE(self) :

        return self.__e

    # f를 반환하는 함수
    def getF(self) :

        return self.__f

    # ad-bc가 0인지 아닌지 판별하는 함수
    def isSolvable(self) :

        # ad-bc가 0이 아니면
        if self.__a * self.__d - self.__b * self.__c != 0 :

            # true를 반환
            return True

        # ad-bc가 0이면
        else :

            # false를 반환
            return False

    # x를 반환하는 함수
    def getX(self) :

        return (self.__e * self.__d - self.__b * self.__f) / (self.__a * self.__d - self.__b * self.__c)

    # y를 반환하는 함수
    def getY(self) :

        return (self.__a * self.__f - self.__e * self.__c) / (self.__a * self.__d - self.__b * self.__c)
