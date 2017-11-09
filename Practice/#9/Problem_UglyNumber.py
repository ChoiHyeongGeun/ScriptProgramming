# Ugly Number

class Solution:
    # @param {int} num an integer
    # @return {boolean} true if num is an ugly number or false
    def isUgly(self, n):
        # Write your code here
        if n <= 0 : return False # n이 0이하이면 return False
        if n == 1 : return True # n이 1이면 return True (ugly number)
        while(n % 2 == 0) : n /= 2 # n이 2로 안나눠떨어질때까지 2로 나눈다.
        while(n % 3 == 0) : n /= 3 # n이 3으로 안나눠떨어질때까지 3으로 나눈다.
        while(n % 5 == 0) : n /= 5 # n이 5로 안나눠떨어질때까지 5로 나눈다.
        return n == 1 # n의 결과가 1이면 return True, 1이 아니면 return False
