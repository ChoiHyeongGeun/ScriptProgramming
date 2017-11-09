# 10.12 : 최대공약수 계산하기

# 약수들을 구해서 list에 저장하는 함수
def prime(number) :

    # 빈 리스트
    list1 = []

    # 1 부터 number까지 반복
    for i in range(1, number+1) :

        # number가 i로 나누어 떨어지면
        if number % i == 0 :

            # 약수이므로 list1에 추가
            list1.append(i)

    # list1을 반환
    return list1

# 최대공약수를 구하여 출력하는 함수
def gcd(number) :

    # number리스트의 0번째 숫자의 약수들을 저장
    list2 = [] + prime(number[0])

    # number리스트의 1번째 숫자의 약수들을 저장
    list3 = [] + prime(number[1])

    # number리스트의 2번째 숫자의 약수들을 저장
    list4 = [] + prime(number[2])

    # number리스트의 3번째 숫자의 약수들을 저장
    list5 = [] + prime(number[3])

    # number리스트의 4번째 숫자의 약수들을 저장
    list6 = [] + prime(number[4])

    # 결과를 저장할 리스트 (빈 리스트)
    list7 = []

    # list2의 원소 개수만큼 반복
    for i in range(len(list2)) :

        # list2[i]가 list3, list4, list5, list6에도 존재한다면
        if (list2[i] in list3) and (list2[i] in list4) and (list2[i] in list5) and (list2[i] in list6) :

            # 그것은 공약수이므로 list2에 추가
            list7.append(list2[i])

    # 공약수들 중에서 가장 큰 수를 출력한다.
    print(list7[len(list7)-1])

# 메인 함수
def main() :

    # 숫자들을 입력받아서 string형으로 저장
    s = input("숫자 5개를 입력하세요 : ")

    # 공백을 구분자로 설정하여 쪼갠 뒤 item에 저장
    items = s.split()

    # items의 원소들을 숫자로 변경하여 list1에 저장
    list1 = [eval(x) for x in items]

    # list1의 최대공약수를 구한다.
    gcd(list1)

# 메인함수 호출
main()
