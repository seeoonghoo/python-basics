# 문제2. 다음과 같은 텍스트에서 모든 태그를 제외한 텍스트만 출력하세요.

s = """
<html>
    <body style='background-color:#ffff'>
        <h4>Click</h4>
        <a href='http://www.python.org'>Here</a>
        <p>
        	To connect to the most powerful tools in the world.
        </p>
    </body>
</html>"""

test = 1
tmp = ''
for i in s:
    if i == '<':
        test = 1

    if test == 1:
        s = s.replace(s,'')
        if i == '>':
            s = s.replace(s,'')
            test = 0
    else:
        tmp += i

print(tmp)
