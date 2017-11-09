# 2.5 : 금융 애플리케이션(팁 계산하기)

# 소계와 팁 비율을 직접 입력받는다.
value, tipRate = eval(input("소계와 팁 비율을 입력하세요 : "))

# 팁을 계산한다.
tip = value * tipRate * 0.01

# 총액을 계산한다.
total = value + tip

# 결과를 출력한다.
print("팁은", tip, "이고 총액은", int(total * 100) / 100.0, "입니다.")
