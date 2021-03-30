# 주어진 if 문을 dict를 사용해서 수정하세요.

menu = input('메뉴 : ')
food = {'오뎅' : 300, '순대' : 400, '만두' : 500}

if menu == '오뎅':
    price = food.get('오뎅')
elif menu == '순대':
    price = food.get('순대')
elif menu == '만두':
    price = food.get('만두')
else:
    price = 0

print('가격 : {0}'.format(price))