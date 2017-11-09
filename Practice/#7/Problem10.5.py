# 10.5 : 고유 숫자 출력하기

# string형으로 숫자들을 입력받는다.
s = input("숫자를 입력하세요 : ")

# 공백을 구분자로 설정하여 items에 저장한다.
items = s.split()

# items의 원소들을 숫자로 변경하여 list1에 저장한다.
list1 = [eval(x) for x in items]

# list2를 공백리스트로 지정한다.
list2 = []

# list1의 원소의 개수만큼 반복문을 실행한다.
for x in range(len(list1)) :

    # list1의 x번째 원소가 list2에 없을 경우에만
    if list1[x] not in list2 :

        # list2에 숫자를 넣는다.
        list2.append(list1[x])

# list2의 모든 원소를 출력한다.
for i in range(len(list2)) :

    print(list2[i], end=' ')
