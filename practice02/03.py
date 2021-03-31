# 문제3. 다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.','\n'를 없앤 후에 중복 없이 각 단어를 순서대로 출력하세요.
# 각 단어의 빈도수도 함께 출력해 보세요

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

for i in s:
    if i == '.' or i ==',' or i=='\n':
        s = s.replace(i,'')
s = s.upper()
s = s.split(' ')
tmp = sorted(s)

for i in tmp:
    print(i)

dic = {}
for i in tmp:
    sum = tmp.count(i)
    dic[i] = sum

for i,j in zip(dic.keys(),dic.values()):
    print(i , ' : ' , j)