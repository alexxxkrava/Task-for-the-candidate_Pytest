class Engine_2D:
    def __init__(self):
        self.canvas = []
    def add_figure(self, figure):
        self.canvas.append(figure)
    def set_color(self, color):
        self.color = color
    def draw(self):
        print(f'Figure color {self.color}')
        for figure in self.canvas:
            print(f'{figure.draw()}.')
        self.canvas = []
class Circle:
    def __init__(self, x, y, radius):
        self.x = x
        self.y = y
        self.radius = radius
    def draw(self):
        return f'Drawing circle: ({self.x}, {self.y}) with radius {self.radius}'
class Triangle:
    def __init__(self, x1, y1, x2, y2, x3, y3):
        self.coordinates = [(x1, y1),(x2, y2),(x3, y3)]
    def draw(self):
        return f"Drawing triangle with coordinates: {', '.join([f'({x}, {y})' for x, y in self.coordinates])}"
class Rectangle:
    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        self.coordinates = [(x1, y1), (x2, y2), (x3, y3), (x4, y4)]
    def draw(self):
        return f"Drawing rectangle with coordinates: {', '.join([f'({x}, {y})' for x, y in self.coordinates])}"
