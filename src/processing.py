def filter_by_state(data: list, state: str = "EXECUTED") -> list:
    """
    Функция, которая перебирает полученный список с помощью state
    и возвращает новый список с нужным значением
    """
    expected_states = []
    for state_dict in data:
        if state_dict["state"] == state:
            expected_states.append(state_dict)
    return expected_states


def sort_by_date(data: list, is_reversed: bool = True) -> list:
    """Функция, которая сортирует полученный список и возвращает новый в указанном порядке"""
    sorted_data = sorted(data, key=lambda x: x["date"], reverse=is_reversed)
    return sorted_data
