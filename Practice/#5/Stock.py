# Stock 클래스 생성
class Stock :

    # 생성자
    def __init__(self, symbol = " ", name = " ", previousClosingPrice = 0.0, currentPrice = 0.0) :

        # private String 데이터필드 : 주식 코드
        self.__symbol = symbol
        
        # private String 데이터필드 : 주식 종목명
        self.__name = name
        
        # private float 데이터필드 : 전일 주식 마감 가격
        self.__previousClosingPrice = previousClosingPrice
        
        # private float 데이터필드 : 현재 시각 주식 가격
        self.__currentPrice = currentPrice

    # 주식 코드를 설정하는 함수
    def setSymbol(self, s) :

        self.__symbol = s

    # 주식 코드를 반환하는 함수
    def getSymbol(self) :

        return self.__symbol

    # 주식 종목명을 설정하는 함
    def setName(self, n) :

        self.__name = n

    # 주식 종목명을 반환하는 함수
    def getName(self) :

        return self.__name

    # 전일 주식 마감 가격을 설정하는 함수
    def setPreviousClosingPrice(self, price) :

        self.__previousClosingPrice = price

    # 전일 주식 마감 가격을 반환하는 함수
    def getPreviousClosingPrice(self) :

        return self.__previousClosingPrice

    # 현재 시각 주식 가격을 설정하는 함수
    def setCurrentPrice(self, price) :

        self.__currentPrice = price
    
    # 현재 시각 주식 가격을 반환하는 함수
    def getCurrentPrice(self) :

        return self.__currentPrice

    # 전일 주식 마감 가격에서 현재 시각 주식 가격으로 변화된 비율을 반환하는 함수
    def getChangePercent(self) :

        return (self.__currentPrice - self.__previousClosingPrice) / 100
