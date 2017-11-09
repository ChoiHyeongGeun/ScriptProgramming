# Happy Number

class Solution:
    # @param {int} n an integer
    # @return {boolean} true if this is a happy number or false
    def isHappy(self, n):
        # Write your code here
        sumList = [] # 각 자리수의 제곱의 합들을 저장할 리스트
        while True : # 무한 반복
           values = [int(i) for i in str(n)] # n을 str형으로 변환 후 각 자리수를 int형으로 저장
           n = sum(i**2 for i in values) # n = values에 있는 값을 제곱하여 모두 더한 값
           if n == 1 : return True # n == 1 이면 return True (Happy num)
           elif n in sumList : return False # n이 sumList에 있으면 return False (Unhappy num)
           sumList.append(n) # 위 2가지에 해당이 안되면 n을 sumList에 추가
