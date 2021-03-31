# 문제1. 파이썬 경로명 s = '/usr/local/bin/python' 에서 각각의 디렉토리 경로명을 분리하여 출력하세요.
# 또, 디렉토리 경로명과 파일명을 분리하여 출력하세요.

s = '/usr/local/bin/python'
print(s.split('/'))
for i in s.split('/'):
    if i != '':
        print(i, end = ' ')

print()

for i in s.rsplit('/',1):
    print (i, end = ' ')

