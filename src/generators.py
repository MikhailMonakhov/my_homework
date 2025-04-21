from typing import Any, Dict, Iterator, List, Optional

# from typing import Callable


def filter_by_currency(transactions: List[Dict[str, Any]], currency: str = "USD") -> Iterator[Dict[str, Any]]:
    """Функция, которая возвращает итератор, фильтрующий список словарей по значению currency"""

    def filtered(transaction: Dict[str, Any]) -> Any:
        """
        Функция внутри filter_by_currency, которая по определённым ключам
        сравнивает значение словаря с заданной валютой в currency(по умолчанию - USD)
        """
        return transaction.get("operationAmount", {}).get("currency", {}).get("code") == currency

    return filter(filtered, transactions)


def transaction_descriptions(transactions: List[Dict[str, Any]]) -> Iterator[Optional[str]]:
    """Функция, которая безопасным образом достаёт значение ключа description"""
    for transaction in transactions:
        yield transaction.get("description")


def card_number_generator(start: int = 0, stop: int = 10**16) -> Iterator[str]:
    """
    Функция, которая может генерировать числа от 1 до 9999.9999.9999.9999, имея при этом
    возможность установить начало и конец(start и stop) в рамках данных значений
    Если значения начала и конца находятся вне рамок, такие числа игнорируются
    """
    for number in range(start, stop + 1):
        if number <= 0 or number >= 10**16:
            continue
        formatted_number = f"{number:016d}"
        yield " ".join([formatted_number[i : i + 4] for i in range(0, 16, 4)])

