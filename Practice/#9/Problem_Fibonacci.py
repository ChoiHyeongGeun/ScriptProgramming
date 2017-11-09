# Fibonacci

class Solution:
    # @param n: an integer
    # @return an integer f(n)
    def fibonacci(self, n):
        # write your code here
        f = [0, 1] # 피보나치 1번째 값 = 0, 2번째 값 = 1
        if n <= 1 : return f[0] # n이 1 이하이면, return f[0]
        else : # n이 2 이상이면
            for i in range(2, n) : # 2부터 n까지 반복
                f.append(f[i-2] + f[i-1]) # f[i-2] + f[i-1] 저장
            return f[len(f)-1] # f 리스트의 마지막 숫자 반환
