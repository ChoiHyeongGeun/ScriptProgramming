# 2.19 : 금융 어플리케이션 (미래 투자가치 계산하기)

# 투자금을 직접 입력받는다.
investment = eval(input("투자금을 입력하세요 : "))

# 연이율을 직접 입력받는다.
interest = eval(input("연이율을 입력하세요 : "))

# 년수를 직접 입력받는다.
year = eval(input("년수를 입력하세요 : "))

# 미래투자가치를 계산하여 저장한다.
price = investment * (1 + (interest / 1200)) ** (12 * year)

# 결과를 출력한다.
print("누적된 가치는", int(price * 100) / 100.0, "입니다.")
