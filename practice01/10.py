# 숫자를 입력 받아서 아래와 같은 실행결과가 나타나도록 코드를 완성하세요.

num = int(input('숫자를 입력하세요 : '))
sum = 0
if num % 2 == 0:
    for i in range(2,num+1,2):
       sum += i
else:
    for i in range(1,num+1,2):
        sum += i

print('결과 값 : ', sum)