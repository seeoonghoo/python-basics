from class_test.Point import Point

class ColorPoint(Point):
    def __init__(self, color, x, y):
        super().__init__(x,y) #부모의 생성자를 가져옴.
        self.color = color

    def draw(self):
        print(f'color={self.color}, x={self.x}, y={self.y} 에 점을 그렸습니다.')