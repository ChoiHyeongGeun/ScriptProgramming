#7.2

# Stock 모듈의 Stock 클래스 사용
from Stock import Stock

# 메인 함수
def main() :

    # 객체1
    s1 = Stock()

    # 객체1 설정
    # 주식 종목 코드 : ABC
    # 주식 종목명 : DEF
    # 전일 가격 : 100
    # 현재 가격 : 200
    s1.setSymbol("INTC")
    s1.setName("Intel Corporation")
    s1.setPreviousClosingPrice(20500)
    s1.setCurrentPrice(20350)

    # 결과 출력
    print("**** 객체1 ****")
    print("주식코드 :", s1.getSymbol())
    print("주식명   :", s1.getName())
    print("전일가격 :", s1.getPreviousClosingPrice())
    print("현재가격 :", s1.getCurrentPrice())
    print("변화비율 :", s1.getChangePercent())


# 메인 함수 출력
main()
