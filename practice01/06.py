# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권,
# 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.

num = int(input('금액 : '))

oman = num // 50000
num = num - oman * 50000
man = num // 10000
num = num - man * 10000
ocheon = num // 5000
num = num - ocheon * 5000
cheon = num // 1000
num = num - cheon * 1000
obaek = num // 500
num = num - obaek * 500
baek = num // 100
num = num - baek * 100
osip = num // 50
num = num - osip * 50
sip = num // 10
num = num - sip * 10
ooo = num // 5
num = num - ooo * 5
ill = num

print('50000원 :', oman)
print('10000원 :', man)
print('5000원:', ocheon)
print('1000원:', cheon)
print('500원:', obaek)
print('100원:', baek)
print('50원:',osip)
print('10원:',sip)
print('5원:',ooo)
print('1원:',ill)
