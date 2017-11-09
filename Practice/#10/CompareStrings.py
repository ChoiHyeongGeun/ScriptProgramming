def compareStrings(self, A, B):
    # write your code here
    lstA = [x for x in A] # A의 내용을 저장
    lstB = [x for x in B] # B의 내용을 저장
    for i in range(len(lstB)) : 
        # lstB[i]가 lstA에 있다면
        if lstB[i] in lstA : 
            # lstA에서 lstB[i] 삭제
            lstA.pop(lstA.index(lstB[i]))
        # lstB[i]가 lstA에 없다면
        else : 
            return False # False 반환
    return True # True 반환
