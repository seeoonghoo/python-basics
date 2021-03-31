# 문제 4. 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

clap = '짝'
for i in range(1,100):
    cnt = 0
    cnt = str(i).count('3') + str(i).count('6') + str(i).count('9')

    if cnt != 0:
        print(i, ' ', clap * cnt)