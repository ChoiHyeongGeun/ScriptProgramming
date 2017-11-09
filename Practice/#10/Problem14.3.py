# 파이썬 키워드들을 갖는 리스트
keyWords = ["and", "as", "assert", "break", "class",
            "continue", "def", "del", "elif", "else", 
            "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"]
# try
try :
    # 파일명 입력
    filename = input("파이썬 소스 코드의 파일명을 입력하세요 : ")
    infile = open(filename, "r", encoding='UTF8') # 파일 열기
    lst = [] + infile.readlines() # 파일의 각 라인들을 갖는 리스트
    dic = {} # 빈 딕셔너리

    for i in range(len(lst)) :
        line = lst[i].split() # 라인 한 줄을 공백을 기준으로 쪼갬
        for j in range(len(keyWords)) :
            n = line.count(keyWords[j]) # 키워드의 개수 카운트
            dic[keyWords[j]] = dic.get(keyWords[j], 0) + n # 딕셔너리에 저장

    # 결과 출력
    for i in range(len(dic)) :
        print(format(keyWords[i], "10s") # 키워드와 키워드의 개수 출력
              , " : ", dic[keyWords[i]], "개")
        
    infile.close() # 파일 닫기
    
# 예외처리
except IOError :
    print("파일이 존재하지 않습니다")
