from class_test.ColorPoint import ColorPoint
from class_test.Point import Point

p1 = Point(10,20)
p1.draw()

p2 = ColorPoint('red',30,50)
p2.draw()

print(type(p2))
print(p2) #__str__ 로 정의한게 이렇게 객체를 프린트하면 나옴


print(Point.count_of_instance)