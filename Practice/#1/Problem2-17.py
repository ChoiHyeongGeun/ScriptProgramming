# 2.17 : 건강 애플리케이션 (BMI 계산하기)

# 파운드를 직접 입력받아서 저장한다.
pound = eval(input("몸무게를 파운드로 입력하세요 : "))

# 입력받은 파운드를 킬로그램으로 변환한다.
kilogram = pound * 0.45359237

# 인치를 직접 입력받아서 저장한다.
inch = eval(input("키를 인치로 입력하세요 : "))

# 입력받은 인치를 미터로 변환한다.
meter = inch * 0.0254

# bmi지수를 식에 알맞게 계산한다.
bmi = kilogram / (meter ** 2)

# 결과를 출력한다.
print("BMI는", int(bmi * 10000) / 10000.0, "입니다.")
