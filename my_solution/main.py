from original.main import Shop, Store, Request
from utils import logistic, print_statistic
from help_class import CheckProduct


def main():
    while (True):
        user_input = input("Enter request: ")

        if user_input == "stop":
            break

        try:
            request = Request(user_input)
        except Exception as e:
            print(f"Некорректный запрос: {e}")
            continue

        from_ = store if request.from_ == "склад" else shop
        to = store if request.to == "склад" else shop

        product = CheckProduct(from_, to, request)

        if not product.is_product_from() \
                or not product.is_product_to() \
                or not product.is_product_unique():
            continue

        logistic(request)

        from_.remove(request.product, request.amount)
        to.add(request.product, request.amount)

        print_statistic(from_)
        print_statistic(to)


if __name__ == "__main__":
    store = Store()
    shop = Shop()
    store_items = {
        "Лимонад": 12,
        "Рояль": 8,
        "Носки": 10,
        "Томаты": 15,
        "Киви": 12,
        "Шашлычок": 5
    }
    store.items = store_items

    main()
