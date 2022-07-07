def logistic(request):
    print(f"Курьер забрал {request.amount} {request.product} из пункта {request.from_}\n"
          f"Курьер везет {request.amount} {request.product} из пункта {request.from_} в пункт {request.to}\n"
          f"Курьер доставил {request.amount} {request.product} в пункт {request.to}")


def print_statistic(place):
    print("=" * 50)

    print(f"В пункте: {place}")
    for title, count in place.items.items():
        print(f"{title}: {count}")
    print(f"Свободного места: {place.get_free_space}")
