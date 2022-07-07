class CheckProduct:
    def __init__(self, from_, to, request):
        self.from_ = from_
        self.to = to
        self.request = request

    def is_product_from(self):
        if self.request.product in self.from_.items:
            print(f"Товар есть в пункте '{self.request.from_}'")
            if self.from_.items[self.request.product] >= self.request.amount:
                print(f"Нужное количетсво есть в пункте '{self.request.from_}'")
                return True
            else:
                print(f"В пункте '{self.request.from_}' не хватает "
                      f"{self.request.amount - self.from_.items[self.request.product]}")
        else:
            print(f"В пункте '{self.request.from_}' нет такого товара")

    def is_product_to(self):
        if self.to.get_free_space >= self.request.amount:
            print(f"В пункте '{self.request.to}' достаточно места")
            return True
        else:
            print(f"В пункте {self.request.to} не хватает {self.request.amount - self.to.get_free_space}")

    def is_product_unique(self):
        if self.request.to == "магазин" \
                and self.to.get_unique_items_count == 5 \
                and self.request.product not in self.to.items:
            print(f"В магазине достаточно уникальных продуктов")
            return False
        else:
            return True
