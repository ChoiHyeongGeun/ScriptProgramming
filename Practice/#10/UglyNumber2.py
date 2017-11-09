def nthUglyNumber(self, n):
    # write your code here
    arr = [] # 빈 리스트
    arr.append(1) # arr에 1 추가
    x = y = z = 0 # 2, 3, 5로 곱해진 횟수
    while len(arr) < n : 
        num2 = arr[x] * 2 # arr[x]에 2를 곱한 값
        num3 = arr[y] * 3 # arr[y]에 3을 곱한 값
        num5 = arr[z] * 5 # arr[z]에 5를 곱한 값
        number = min(num2, num3, num5) # 3개 중 최소값
        if number == num2 : # 최소값이 num2이면
            x += 1 # x 1증가
        elif number == num3 : # 최소값이 num3이면 
            y += 1 # y 1증가
        elif number == num5 : # 최소값이 num4이면
            z += 1 # z 1증가
        if number not in arr : # 최소값이 arr에 없다면
            arr.append(number) # 최소값 추가
    return arr[n-1] # 마지막 값 반환
