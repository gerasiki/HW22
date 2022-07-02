class Cube:

    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z

    def get_volume(self):
        return self.x * self.y * self.z


class CubeVolumeCalculator:

    @staticmethod
    def calc_cube_volume(cube):
        return cube.get_volume()


if __name__ == '__main__':
    new_cube = Cube(4, 4, 4)  # по-моему, стороны куба всегда одинаковые
    my_cube = CubeVolumeCalculator()
    print(my_cube.calc_cube_volume(new_cube))
