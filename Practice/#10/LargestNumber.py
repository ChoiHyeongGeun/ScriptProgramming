def largestNumber(self, num):
    # write your code here
    s1 = [str(x) for x in num] # num 내용을 str형변환 후 저장
    # 숫자 a와 b가 있을때 ab와 ba를 비교 후 큰 순서대로 정렬
    for i in range(0, len(num)-1) : # 0 ~ 마지막인덱스-1
        for j in range(i, len(num)) : # i ~ 마지막인덱스
            # 1. s1[i]와 s1[j] 둘 다 0일 때
            if s1[i] == "0" and s1[j] == "0" : 
                ij = ji = "0" # ij = ji = 0
            # 2. s1[i]만 0일 때
            elif s1[i] == "0" and s1[j] != "0" : 
                ij = s1[j] # ij = s1[j]
                ji = s1[j] + s1[i] # ji = s1[j]s1[i]
            # 3. s1[j]만 0일 때
            elif s1[i] != "0" and s1[j] == "0" : 
                ij = s1[i] + s1[j] # ij = s1[i]s1[j]
                ji = s1[i] # ji = s1[i]
            # 4. 둘 다 0이 아닐 때
            else : 
                ij = s1[i] + s1[j] # ij = s1[i]s1[j]
                ji = s1[j] + s1[i] # ji = s1[j]s1[i]
            # ij와 ji를 비교하여 ji가 더 크다면
            # s1[i]와 s1[j]를 교체
            if eval(ji) > eval(ij) : 
                n = s1[j] # s1[j]를 n에 저장
                s1.pop(j) # s1[j] 삭제
                s1.insert(i, n) # i번째에 n 삽입
    result = "" # 결과
    for i in range(len(s1)) : 
        # result가 ""이고 s1[i]가 0일 때
        if result == "" and s1[i] == "0" :
            # 1. i가 마지막인덱스라면
            if i == len(s1)-1 : return "0" # 그대로 0 반환
            # 2. i가 마지막인덱스가 아니라면
            else : continue # result에 추가하지 않음
        # result가 ""이 아니라면
        else : result = result + s1[i] # result에 s1[i] 추가
    return result # result 반환
