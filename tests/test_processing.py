from src.processing import filter_by_state


def test_filter_by_state_with_executed(sample_list_of_data_base: list, state_executed: str,
                                       list_of_data_base_with_state_executed: list) -> None:
    """Тестирование функции с параметром "state: "EXECUTED" """
    assert filter_by_state(sample_list_of_data_base, state_executed) == list_of_data_base_with_state_executed


def test_filter_by_state_without_state(sample_list_of_data_base: list,
                                       list_of_data_base_with_state_executed: list) -> None:
    """Тестирование функции без указания параметра "state" """
    assert filter_by_state(sample_list_of_data_base) == list_of_data_base_with_state_executed


def test_filter_by_state_canceled(sample_list_of_data_base: list, state_canceled: str,
                                  list_of_data_base_with_state_canceled: list) -> None:
    """Тестирование функции с параметром "state: "CANCELED" """
    assert filter_by_state(sample_list_of_data_base, state_canceled) == list_of_data_base_with_state_canceled


def test_filter_by_state_without_state_in_list(sample_list_of_data_base_executed_without_state: list,
                                               list_of_data_base_with_state_executed: list) -> None:
    """Тестирование функции без указания параметра "state" """
    assert filter_by_state(sample_list_of_data_base_executed_without_state) == list_of_data_base_with_state_executed
