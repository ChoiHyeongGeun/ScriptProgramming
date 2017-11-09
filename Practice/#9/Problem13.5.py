# 13.5 : 문자열 대체하기

try :
    # 파일이름, 교체전 문자열, 교체될 문자열을 입력받는다.
    filename = input("파일명을 입력하세요 : ")
    st1 = input("교체될 이전 문자열을 입력하세요 : ")
    st2 = input("이전 문자열을 대체할 새로운 문자열을 입력하세요 : ")

    # 파일을 읽기 용도로 연다.
    infile = open(filename, "r")

    # content1 : 교체전 파일의 내용을 저장한 리스트
    # content2 : 교체후 파일의 내용을 저장할 리스트
    content1 = [] + infile.readlines()
    content2 = []

    # content1의 개수(파일의 line 수)만큼 반복문 실행
    for i in range(len(content1)) :
        line = content1[i] # i번째 내용을 문자열로 저장
        newline = line.replace(st1, st2) # st1을 st2로 교체 후 저장
        content2.append(newline) # 교체된 문자열을 content2에 추가
            
    infile.close() # 파일 닫기

    # 파일을 쓰기 용도로 연다. (기존의 파일은 덮어쓴다.)
    outfile = open(filename, "w")

    # content2의 개수(파일의 line 수)만큼 반복문 실행
    for i in range(len(content2)) :
        outfile.write(content2[i]) # 파일에 내용을 쓴다.

    outfile.close() # 파일 닫기
 
    print("완료되었습니다.") # 완료 메시지

except IOError : # 파일이 없을 경우 에러메시지
    print("파일이 존재하지 않습니다.")
