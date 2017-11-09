# 13.6 : 단어 개수 세기

# urllib.request 모듈 사용
import urllib.request

# 웹 주소를 이용하여 데이터 저장
infile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Lincoln.txt")

content = [] + infile.readlines() # infile 내용을 리스트로 저장할 리스트
sort = [] # 존재하는 단어들을 저장할 리스트 (중복 허용)
word = [] # 존재하는 단어들을 저장할 리스트 (중복 제거)
num = [] # 단어들의 개수를 저장할 리스트

# content 리스트의 요소의 개수만큼 반복
for i in range(len(content)) :
    code = content[i].split() # content[i]를 공백을 기준으로 쪼갠 뒤 저장

    # code 리스트의 요소의 개수만큼 반복
    for j in range(len(code)) :
        sort.append(code[j].decode()) # code[j]를 decode하여 sort 리스트에 저장

n = 0 # n : while 문에서 사용할 인덱스
while n < len(sort) : # n이 sort 리스트의 요소의 개수보다 작으면 반복

    # 단어에 마침표 또는 쉼표가 있으면 제거한다.
    removeDot = sort[n].replace(".", "") # sort[n]에서 마침표를 제거 후 저장
    remove = removeDot.replace(",", "") # removeDot에서 쉼표를 제거 후 저장
    lowercase = remove.lower() # 단어를 모두 소문자로 변경
    sort.pop(n) # n번째 단어 삭제
    sort.insert(n, lowercase) # n번째에 remove 추가

    # 마침표와 쉼표를 제거한 후에도 특수문자가 존재한다면
    if sort[n].isalnum() == False :
        sort.pop(n) # 단어가 아니므로 n번째 단어 삭제
    # 마침표와 쉼표를 제거한 후에 특수문자가 존재하지 않는다면
    else :
        n += 1 # 인덱스 1 증가

n = 0 # 인덱스 초기화
while len(sort) > 0 : # sort에 요소가 존재한다면 반복
    text = sort[n] # text : n번째 단어
    word.append(text) # word 리스트에 text를 추가
    num_text = sort.count(text) # num_text : sort에 존재하는 text의 개수
    num.append(num_text) # num 리스트에 text의 개수 추가
    for i in range(num_text) : # num_text 만큼 반복
        index = sort.index(text) # text가 존재하는 인덱스 반환
        sort.pop(index) # 해당 인덱스의 단어(text) 삭제

# 결과 출력
for i in range(len(word)) :
    print("[단어 :", format(word[i], '>12s'), end='')
    print("]   [개수 :", format(num[i], '2d'), "개]")
