# MyTriangle

# math 모듈을 사용한다.
import math


# 세 변이 삼각형을 이루는지 확인하는 함수
def isValid(side1, side2, side3) :

    # side3이 가장 긴 변이고 side3이 나머지 두 변의 합보다 작으면
    if (side3 >= side1) and (side3 >= side2) and (side1 + side2 > side3) :

        # 삼각형을 이룬다.
        return True

    # side2이 가장 긴 변이고 side2이 나머지 두 변의 합보다 작으면
    elif (side2 >= side1) and (side2 >= side3) and (side1 + side3 > side2) :

        # 삼각형을 이룬다.
        return True

    # side1이 가장 긴 변이고 side1이 나머지 두 변의 합보다 작으면
    elif (side1 >= side2) and (side1 >= side3) and (side3 + side2 > side1) :

        # 삼각형을 이룬다.
        return True
    
    # 가장 긴 변이 나머지 두 변의 합보다 크거나 같으면
    else :

        # 삼각형을 이루지 않는다.
        return False


# 삼각형의 넓이를 구하는 함수
def area(side1, side2, side3) :

    # 세 변이 삼각형을 이루면
    if isValid(side1, side2, side3) == True : 

        # 넓이를 구한다.
        s = (side1 + side2 + side3) / 2
        area = math.sqrt(s * (s-side1) * (s-side2) * (s-side3))

        # 결과를 출력한다.
        print("삼각형의 넓이는", area, "입니다.")

    # 세 변이 삼각형을 이루지 않으면
    else :

        # 에러 메시지를 출력한다.
        print("잘못된 입력입니다.")
