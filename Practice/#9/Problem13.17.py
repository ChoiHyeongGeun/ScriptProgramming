# 13.17 : 대용량 데이터 처리하기

# urllib.request 모듈 사용
import urllib.request

# 웹 주소를 이용하여 데이터 저장
infile = urllib.request.urlopen("http://cs.armstrong.edu/liang/data/Salary.txt")

lst = [] + infile.readlines() # infile 내용을 저장할 리스트
name_code = [] # lst를 공백으로 구분하여 split한 후 저장할 리스트
name = [] # name_code를 decode하여 저장할 리스트
assistant_salary = 0.0 # 조교수 연봉 총합
assistant_num = 0 # 조교수 수
associate_salary = 0.0 # 부교수 연봉 총합
associate_num = 0 # 부교수 수
full_salary = 0.0 # 정교수 연봉 총합
full_num = 0 # 정교수 수
prof_salary = 0.0 # 모든 교수 연봉 총합

for i in range(len(lst)) : # lst의 요소의 개수만큼 반복
    name_code = lst[i].split() # 요소를 공백으로 구분하여 저장

    for j in range(len(name_code)) : # name_code의 요소의 개수만큼 반복
        name.append(name_code[j].decode()) # 요소를 decode하여 저장

for i in range((int)(len(name)/4)) : # name의 요소의 개수의 1/4만큼 반복
    prof_salary += eval(name[4*i + 3]) # 연봉을 모두 더한다.
    
    if name[4*i + 2] == "assistant" : # 조교수 연봉이면
        assistant_num += 1 # 조교수 수 1 증가
        assistant_salary += eval(name[4*i + 3]) # 조교수 연봉에 더한다.

    elif name[4*i + 2] == "associate" : # 부교수 연봉이면
        associate_num += 1 # 부교수 수 1 증가
        associate_salary += eval(name[4*i + 3]) # 부교수 연봉에 더한다.

    elif name[4*i + 2] == "full" : # 정교수 연봉이면
        full_num += 1 # 정교수 수 1 증가
        full_salary += eval(name[4*i + 3]) # 정교수 연봉에 더한다.

# 결과 출력
print("  조교수 평균 연봉 :", assistant_salary / assistant_num)
print("  부교수 평균 연봉 :", associate_salary / associate_num)
print("  정교수 평균 연봉 :", full_salary / full_num)
print("모든교수 평균 연봉 :", prof_salary / len(name))
