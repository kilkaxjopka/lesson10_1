from typing import Dict, List


def filter_by_state(test: List[Dict], state: str = "EXECUTED") -> List[Dict]:
    """Фильтрует список словарей по указанному состоянию"""
    return [d for d in test if d.get("state") == state]


def sort_by_date(test: List[Dict], order: str = "desc") -> List[Dict]:
    """Сортирует список словарей по полю 'date'"""
    if order == "desc":
        return sorted(test, key=lambda x: x["date"], reverse=True)
    else:
        return sorted(test, key=lambda x: x["date"])


# Пример использования
test = [
    {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
    {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
    {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
    {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
]

filtered_data = filter_by_state(test)
sorted_data = sort_by_date(test)
