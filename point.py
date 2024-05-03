class Point:
    def __init__(self, x=0, y=0):
        """Метод для инициализации координат точки, по умолчанию точка имеет координаты [0, 0]."""

        self.x = x
        self.y = y

    def __repr__(self):
        return f'[{self.x}, {self.y}]'

    def get_coordinates(self):
        """Метод для получения координат уже точки в формате [x, y]."""

        return [self.x, self.y]

    def set_coordinates(self, x, y):
        """Метод для изменения координат уже существующей точки."""

        self.x = x
        self.y = y

    def distance(self, second_point):
        """Рассчитывает относительное расстояние до указанной в аргументах точки."""

        x_dist = second_point.get_coordinates()[0] - self.get_coordinates()[0]
        y_dist = second_point.get_coordinates()[1] - self.get_coordinates()[1]
        return [x_dist, y_dist]

