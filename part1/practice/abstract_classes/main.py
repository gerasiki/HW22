from abc import ABC, abstractmethod


class Transport(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def start_engine(self):
        pass

    @abstractmethod
    def stop_engine(self):
        pass

    @abstractmethod
    def move(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Boat(Transport):
    def __init__(self):
        super().__init__()

    def start_engine(self):
        print('Включаем мотор лодки')

    def stop_engine(self):
        print('Выключаем мотор лодки')

    def move(self):
        print('Рассекаем волны')

    def stop(self):
        print('Не рассекаем волны')


class Car(Transport):
    def __init__(self):
        super().__init__()

    def start_engine(self):
        print('Включаем мотор машины')

    def stop_engine(self):
        print('Выключаем мотор машины')

    def move(self):
        print('Мчимся со скоростью 150 км/ч')

    def stop(self):
        print('Не мчимся со скоростью 150 км/ч')


class Electroscooter(Transport):
    def __init__(self):
        super().__init__()

    def start_engine(self):
        print('Включаем мотор скутера')

    def stop_engine(self):
        print('Выключаем мотор скутера')

    def move(self):
        print('Едем, всем мешаем')

    def stop(self):
        print('Стоим на светофоре')


class Person:

    def use_transport(self, transport: Transport):
        transport.start_engine()
        transport.stop_engine()
        transport.move()
        transport.stop()


if __name__ == '__main__':
    boat = Boat()
    car = Car()
    kamikadze = Electroscooter()

    person = Person()
    person.use_transport(boat)
    print('=' * 10)
    person.use_transport(car)
    print('=' * 10)
    person.use_transport(kamikadze)
