# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.

def reverse(s):
    return s.__reversed__()

in_str = input('입력 > ')

print('결과>' + in_str[::-1])