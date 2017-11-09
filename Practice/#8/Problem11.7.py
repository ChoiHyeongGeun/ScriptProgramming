# 11.7 - 가장 가까운 두 점

# math 모듈 사용
import math

# 가장 가까운 두 점을 찾는 함수
def nearest(p) :

    # 두 점의 최소 거리 = 100만으로 초기화
    minLength = 1000000

    # 모든 두 점간의 거리를 구한다.
    for x in range(0, len(p)-1) :

        for y in range(x+1, len(p)) :

            # x2x1 = x1 과 x2 사이의 거리
            # y2y1 = y1 과 y2 사이의 거리
            # z2z1 = z1 과 z2 사이의 거리
            x2x1 = p[y][0] - p[x][0]
            y2y1 = p[y][1] - p[x][1]
            z2z1 = p[y][2] - p[x][2]

            # length = 두 점간의 거리
            length = math.sqrt((x2x1 ** 2) + (y2y1 ** 2) + (z2z1 ** 2))

            # 두 점간의 거리가 현재까지의 최소 거리보다 작다면
            if length < minLength :

                # 최소 거리를 length로 변경하고
                # 최소 거리를 이루는 두 점을 저장한다.
                minLength = length
                point1 = x               
                point2 = y

    # 결과를 출력한다.
    print()
    print("점", point1, " : ", p[x])
    print("점", point2, " : ", p[y])
    print("두 점 사이의 거리 : ", format(minLength, ".5f"))

# 메인 함수
def main() :

    # 3차원 점 리스트
    points = [[-1, 0, 3], [-1, -1, -1], [4, 1, 1], [2, 0.5, 9],
              [3.5, 2, -1], [3, 1.5, 3], [-1.5, 4, 2], [5.5, 4, -0.5]]

    # 함수 실행
    nearest(points)

# 메인 함수 호출
main()
