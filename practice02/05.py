# 문제 5. 함수 sum 을 만드세요. 이 함수는 임의의 개수의 인수를 받아서 그 합을 계산합니다.

def mysum(*args):
    tmp = 0
    for i in args[0]:
        tmp += int(i)
    return tmp


start = []

while 1:
    a = int(input('숫자 입력 하시오 (0 입력시 입력 종료) : '))
    if a == 0:
        break
    else:
        start.append(str(a))


print(mysum(start))