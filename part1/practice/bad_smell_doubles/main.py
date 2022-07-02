class SomeClass:
    def __init__(self):
        self.lst = [3, 2, 1, 4, 2, 1]

    def sorted_func(self, reverse: bool):
        return sorted(self.lst, reverse=reverse)


if __name__ == '__main__':
    items = SomeClass()
    print(items.sorted_func(False))
