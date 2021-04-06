class Point:
    count_of_instance = 0
    def __init__(self,x,y):
        Point.count_of_instance += 1 # 이렇게 클래스로 해서 객체를 해야함, 
        self.x = x
        self.y = y
        # 생성자 함수

    def draw(self):
        print(f'x={self.x}, y={self.y} 에 점을 그렸습니다.')
