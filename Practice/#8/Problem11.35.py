# 11.35 - 중심 도시

# math 모듈 사용
import math

# (x1, y1) 과 (x2, y2) 사이의 거리를 반환하는 함수
def distance(x1, y1, x2, y2) :

    return math.sqrt(((x2 - x1) ** 2) + ((y2 - y1) ** 2))

# 중심 도시를 구하는 함수
def center(c) :

    # 최소거리 = 100만으로 초기화
    # 중심 도시 = 0번째 도시로 초기
    minDistance = 1000000
    minPosition = 0

    # 모든 도시를 체크한다.
    for x in range(0, len(c)) :

        # sum = 한 도시에서 다른 도시들까지의 거리들의 합
        sum = 0

        # 모든 도시를 체크한다.
        for y in range(0, len(c)) :

            # 다른 도시들까지의 합을 구한다.
            sum = sum + distance(c[x][0], c[x][1], c[y][0], c[y][1])

        # 최소거리보다 sum이 작으면
        if minDistance > sum :

            # 최소거리를 sum으로 변경하고
            # 최소거리를 갖는 도시를 저장한다.
            minDistance = sum
            minPosition = x

    # 결과를 출력한다.
    print("중심 도시는 (", c[minPosition][0], ",", c[minPosition][1], ") 에 있습니다.")

# 메인 함수
def main() :

    # 도시의 개수를 입력받는다.
    num = eval(input("도시의 개수를 입력하세요 : "))

    # 도시의 좌표들을 입력받는다.
    s = input("도시의 좌표를 입력하세요 : ")
    items = s.split()
    
    lst = [] # 1차원 리스트
    city = [] # 2차원 리스트

    # items를 city에 2차원 리스트로 저장한다.
    for i in range(len(items)) :

        # items의 내용을 lst에 추가
        lst.append(eval(items[i]))

        # i+1이 2의 배수이면
        if (i+1) % 2 == 0 :

            # city에 lst를 추가하고 lst를 초기화한다.
            city.append(lst)
            lst = []

    # 도시의 개수와 city의 내용의 개수와 같으면 함수 호출
    if num == len(city) :

        center(city)

    # 다르면 에러메시지
    else :

        print("잘못 입력하였습니다.")

# 메인 함수 호출
main()
