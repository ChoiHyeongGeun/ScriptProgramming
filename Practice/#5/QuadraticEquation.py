# math 모듈 사용
import math

# QuadraticEquation 클래스
class QuadraticEquation :

    # 생성자
    def __init__(self, a = 0, b = 0, c = 0) :

        self.__a = a

        self.__b = b

        self.__c = c

    # a를 반환하는 함수
    def getA(self) :

        return self.__a

    # b를 반환하는 함수
    def getB(self) :

        return self.__b

    # c를 반환하는 함수
    def getC(self) :

        return self.__c

    # b^2-4ac(판별식)를 반환하는 함수
    def getDiscriminant(self) :

        return math.pow(self.__b, 2) - 4 * self.__a * self.__c

    # 해1을 반환하는 함수
    def getRoot1(self) :

        # 판별식이 0보다 크거나 같으면
        if self.getDiscriminant() >= 0 : 

            # 해를 반환
            return (-(self.__b) + math.sqrt(math.pow(self.__b, 2) - 4 * self.__a * self.__c)) / 2 * self.__a

        # 판별식이 0보다 작으면
        else :

            # 0을 반환
            return 0

    # 해2를 반환하는 함수
    def getRoot2(self) :

        # 판별식이 0보다 크거나 같으면
        if self.getDiscriminant() >= 0 : 

            # 해를 반환
            return (-(self.__b) - math.sqrt(math.pow(self.__b, 2) - 4 * self.__a * self.__c)) / 2 * self.__a

        # 판별식이 0보다 작으면
        else :

            # 0을 반환
            return 0
