# 키보드에서 5개의 정수를 입력 받아 리스트에 저장하고 평균을 구하는 프로그램을 작성하시오

tmp = []

for i in range(5):
    tmp.append(int(input('>')))

print('평균 : ' , sum(tmp)/5)