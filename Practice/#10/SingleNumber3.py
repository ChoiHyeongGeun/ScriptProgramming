def singleNumberIII(self, A):
    # write your code here
    num = {} # 빈 딕셔너리
    result = [] # 빈 리스트
    for i in range(len(A)) : # A 리스트 내용 개수 만큼 반복
        num[A[i]] = num.get(A[i], 0) + 1 # 숫자와 숫자 개수 삽입
    for i in range(len(A)) : # A 리스트 내용 개수 만큼 반복
        # A[i] 개수가 홀수개이고 A[i]가 result 안에 없으면
        if (num[A[i]] % 2 != 0) and (A[i] not in result): 
            result.append(A[i]) # result에 A[i] 삽입
    if len(result) == 2 : return result # result 개수가 2이면 그대로 반환
    elif len(result) == 1 : # result 개수가 1이면
        result.insert(0, 0) # result에 0을 삽입 후
        return result # 반환
    else : return [0, 0] # [0, 0] 반환
