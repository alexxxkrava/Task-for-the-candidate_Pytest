import pytest
from main_2 import Engine_2D, Circle, Triangle, Rectangle

@pytest.mark.parametrize('color', ['red', 'blue', None, ''])
def test_color(color):
    engine = Engine_2D()
    if color is None or color == '':
        assert False, "Color doesn't exists."
    else:
        engine.set_color(color)

@pytest.mark.parametrize('x, y, radius, expected', [(0, 0, 5, True),
                                                    (0, 0, -5, False), # Радиус < 0 (недопустимо)
                                                    ('a', 0, 5, False),# Недопустимые координаты (не число)
                                                    (0, 0, 'a', False) # Недопустимый радиус (не число)
                                                    ]
                         )
def test_circle_parameters(x, y, radius, expected):
    if expected:
        circle = Circle(x, y, radius)
        result = circle.draw()
        assert result
    else:
        output = "Invalid parameters for circle."
        assert False, output

@pytest.mark.parametrize('x1, y1, x2, y2, x3, y3, expected', [(0, 0, 1, 0, 0, 1, True), # Правильный треугольник
                                                    (0, 0, 1, 0, 2, 0, False), # Невозможно построить треугольник
                                                    (0, 0, 0, 0, 0, 0, False), # Нулевые длины сторон
                                                    (0, 0, 0, 5, 0, 2, False)  # Вершины лежат на одной вертикальной линии, но длины сторон больше нуля
                                                    ]
                         )
def test_triangle_parameters(x1, y1, x2, y2, x3, y3, expected):
    if expected:
        triangle = Triangle(x1, y1, x2, y2, x3, y3)
        result = triangle.draw()
        assert result
    else:
        output = "Invalid parameters for triangle."
        assert False, output

@pytest.mark.parametrize('x1, y1, x2, y2, x3, y3, x4, y4, expected', [(0, 0, 2, 0, 2, 2, 0, 2, True), # Правильный прямоугольник
                                                            (0, 0, 0, 0, 0, 0, 0, 0, False), # Нулевые длины сторон
                                                            (0, 0, 2, 0, 2, 0, 2, 0, False), # Вырожденный прямоугольник
                                                            (0, 0, 1, 1, 2, 2, 3, 3, False), # Вершины не образуют прямоугольник
                                                            (0, 0, 4, 0, 4, 4, 0, 4, True) # Большие значения координат и длин сторон
                                                            ]
                         )
def test_rectangle_parameters(x1, y1, x2, y2, x3, y3, x4, y4, expected):
    if expected:
        rectangle = Rectangle(x1, y1, x2, y2, x3, y3, x4, y4)
        result = rectangle.draw()
        assert result
    else:
        assert False, "Invalid parameters for rectangle"