# 주어진 리스트 데이터를 이용하여 3의 배수의 개수와 배수의 합을 구하여 출력형태와 같이 출력하세요.

tmp = [10,12,14,15,17,18,19,20,25,30,32,33,40,43,44,46,50]
cnt = 0
sum = 0
for i in tmp:
    if i % 3 == 0:
        cnt += 1
        sum += i

print('주어진 리스트에서 3의 배수의 개수=> ', cnt)
print('주어진 리스트에서 3의 배수의 합=> ', sum)