from typing import Any

from src.filter_transactions import search_operation_by_description, transactions_counter_by_type


def test_search_operation_found_by_keyword(sample_transactions_2: list[dict[Any, Any]]) -> Any:
    """Тестирование ввода для ключа "description" """
    results = search_operation_by_description(sample_transactions_2, "карта")
    assert len(results) == 1
    assert results[0]["id"] == 1


def test_search_operation_multiple_matches(sample_transactions_2: list[dict[Any, Any]]) -> Any:
    """Тестирование ввода для ключа "description" """
    results = search_operation_by_description(sample_transactions_2, "счет")
    assert len(results) == 1
    assert results[0]["id"] == 2


def test_search_operation_no_match(sample_transactions_2: list[dict[Any, Any]]) -> Any:
    """Тестирование ввода для ключа "description" """
    results = search_operation_by_description(sample_transactions_2, "неизвестное слово")
    assert results == []


def test_search_operation_case_insensitive(sample_transactions_2: list[dict[Any, Any]]) -> Any:
    """Тестирование ввода для ключа "description" """
    results = search_operation_by_description(sample_transactions_2, "ОрГанИзац")
    assert len(results) == 1
    assert results[0]["id"] == 3


def test_search_operation_description_is_none(sample_transactions_2: list[dict[Any, Any]]) -> Any:
    """Тестирование ввода для ключа "description" """
    results = search_operation_by_description(sample_transactions_2, "вклад")
    assert len(results) == 1
    assert results[0]["id"] == 4


def test_basic_count(sample_transactions_3, categories):
    """Проверка подсчёта количества операций для всех категорий из исходных данных."""
    expected = {
        'Перевод организации': 3,
        'Открытие вклада': 1,
        'Перевод со счета на счет': 2
    }
    assert transactions_counter_by_type(sample_transactions_3, categories) == expected
    

    
