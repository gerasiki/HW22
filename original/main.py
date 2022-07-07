from abc import ABC, abstractmethod


class Storage(ABC):
    @abstractmethod
    def __init__(self, items: dict, capacity: int):
        self._items = items
        self._capacity = capacity

    @abstractmethod
    def add(self, title, count):
        ...

    @abstractmethod
    def remove(self, title, count):
        ...

    @property
    @abstractmethod
    def get_free_space(self):
        ...

    @property
    @abstractmethod
    def items(self):
        ...

    @property
    @abstractmethod
    def get_unique_items_count(self):
        ...


class Store(Storage):
    def __init__(self):
        self._items = {}
        self._capacity = 100

    def add(self, title, count):
        if title in self._items:
            self._items[title] += count
        else:
            self._items[title] = count
        self._capacity -= count

    def remove(self, title, count):
        res = self._items[title] - count
        if res > 0:
            self._items[title] = res
        else:
            del self._items[title]
        self._capacity += count

    @property
    def get_free_space(self):
        return self._capacity

    @property
    def items(self):
        return self._items

    @items.setter
    def items(self, new_items):
        self._items = new_items
        self._capacity -= sum(self._items.values())

    @property
    def get_unique_items_count(self):
        return len(self._items.keys())


class Shop(Store):
    def __init__(self):
        super().__init__()
        self._capacity = 20


class Request():
    def __init__(self, info):
        self.info = self._split_info(info)
        self.from_ = self.info[4]
        self.to = self.info[6]
        self.amount = int(self.info[1])
        self.product = self.info[2]

    @staticmethod
    def _split_info(info):
        return info.split(" ")

    def __repr__(self):
        return f"Доставить {self.amount} {self.product} из {self.from_} в {self.to}"


def main():
    while (True):
        user_input = input("Enter request")

        if user_input == "stop":
            break

        request = Request(user_input)
        store.items = store_items

        from_ = store if request.from_ == "склад" else shop
        to = store if request.to == "склад" else shop

        if request.product in from_.items:
            print(f"Товар есть в пункте '{request.from_}'")
        else:
            print(f"В пункте '{request.from_}' нет такого товара")
            continue

        if from_.items[request.product] >= request.amount:
            print(f"Нужное количетсво есть в пункте '{request.from_}'")
        else:
            print(f"В пункте '{request.from_}' не хватает {request.amount - from_.items[request.product]}")
            continue

        if to.get_free_space >= request.amount:
            print(f"В пункте '{request.to}' достаточно места")
        else:
            print(f"В пункте {request.to} не хватает {request.amount - to.get_free_space}")
            continue

        if request.to == "магазин" and to.get_unique_items_count == 5 and request.product not in to.items:
            print(f"В магазине достаточно уникальных продуктов")
            continue

        from_.remove(request.product, request.amount)
        print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}")
        print(f"Курьер везет {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}")
        to.add(request.product, request.amount)
        print(f"Курьер доставил {request.amount} {request.product} в пункта {request.to}")

        print("=" * 50)

        print("На складе:")
        for title, count in store.items.items():
            print(f"{title}: {count}")
        print(f"Свободного места: {store.get_free_space}")
        print("=" * 50)

        print("В магазине:")
        for title, count in shop.items.items():
            print(f"{title}: {count}")
        print(f"Свободного места: {shop.get_free_space}")

        break


if __name__ == "__main__":
    store = Store()
    shop = Shop()
    store_items = {
        "Лимонад": 12,
        "Рояль": 8,
        "Носки": 10,
        "Томаты": 15
    }

    main()
