# class Room:
#     def get_name(self):
#         return 42
#
#
# class Street:
#     def get_room(self) -> Room:
#         return Room()
#
#
# class City:
#     def get_street(self) -> Street:
#         return Street()
#
#     def population(self):
#         return 100500
#
#
# class Country:
#     def get_city(self) -> City:
#         return City()
#
#
# class Planet:
#     def get_contry(self) -> Country:
#         return Country()


class Person:
    def __init__(self, population, room_num):
        self.population = population
        self.room_num = room_num

    def get_person_room(self):
        return self.room_num

    def get_city_population(self):
        return self.population


person = Person(1000, 38)
print(f'В городе людей: {person.get_city_population()}, '
      f'Наш человек живёт в комнате: {person.get_person_room()}')
