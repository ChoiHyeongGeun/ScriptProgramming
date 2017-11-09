def majorityNumber(self, nums, k):
    # write your code here
    num = {} # 빈 딕셔너리
    max = 0 # 최대 개수
    for i in range(len(nums)) : # nums리스트 내용 개수 만큼 반복
        num[nums[i]] = num.get(nums[i], 0) + 1 # nums[i]의 value값에 + 1 하여 저장
        if num[nums[i]] > max: # nums[i]의 value값이 max보다 크면
            max = num[nums[i]] # max값 변경
            majority_num = nums[i] # majority_num에 키값 대입
    return majority_num # majority_num 반환
