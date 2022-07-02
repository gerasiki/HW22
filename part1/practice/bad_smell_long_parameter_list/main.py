class Unit:
    def __init__(self, x_coord, y_coord, state):
        self.x = x_coord
        self.y = y_coord
        self.state = state

    def get_speed(self, state):
        if state == "fly":
            return self.speed * 1.2
        elif state == "crawl":
            return self.speed * 0.5
        else:
            raise ValueError('Рожденный ползать летать не должен!')

    def move(self, direction, speed):
        self.speed = speed
        object_speed = self.get_speed(self.state)
        if direction == "UP":
            return self._get_unit(x=self.x, y=self.y + object_speed, unit=self)
        elif direction == "DOWN":
            return self._get_unit(x=self.x, y=self.y - object_speed, unit=self)
        elif direction == "LEFT":
            return self._get_unit(x=self.x - object_speed, y=self.y, unit=self)
        elif direction == 'RIGHT':
            return self._get_unit(x=self.x + object_speed, y=self.y, unit=self)

    @staticmethod
    def _get_unit(x, y, unit):
        print(f'location:\nx: {x},\ny: {y},\nobject: {unit}\n')


if __name__ == '__main__':
    #
    # robot = Unit(0, 0, 'crawl')
    # plane = Unit(0, 0, 'fly')
    man = Unit(0, 0, 'crawl')

    # robot.move("LEFT", 20)
    # plane.move("UP", 60)
    man.move('RIGHT', 10)
