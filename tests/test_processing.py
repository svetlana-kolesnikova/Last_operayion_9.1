from src.processing import filter_by_state, sort_by_date


def test_filter_by_state_with_executed(
    sample_list_of_data_base: list, state_executed: str, list_of_data_base_with_state_executed: list
) -> None:
    """Тестирование функции с параметром "state: "EXECUTED" """
    assert filter_by_state(sample_list_of_data_base, state_executed) == list_of_data_base_with_state_executed


def test_filter_by_state_without_state(
    sample_list_of_data_base: list, list_of_data_base_with_state_executed: list
) -> None:
    """Тестирование функции без указания параметра "state" """
    assert filter_by_state(sample_list_of_data_base) == list_of_data_base_with_state_executed


def test_filter_by_state_canceled(
    sample_list_of_data_base: list, state_canceled: str, list_of_data_base_with_state_canceled: list
) -> None:
    """Тестирование функции с параметром "state: "CANCELED" """
    assert filter_by_state(sample_list_of_data_base, state_canceled) == list_of_data_base_with_state_canceled


def test_filter_by_state_without_state_in_list(
    sample_list_of_data_base_executed_without_state: list, list_of_data_base_with_state_executed: list
) -> None:
    """Тестирование функции без указания параметра "state" """
    assert filter_by_state(sample_list_of_data_base_executed_without_state) == list_of_data_base_with_state_executed


def test_sort_by_date(
    sample_list_of_data_base_executed_without_state: list, sample_list_of_data_base_sorted_by_date: list
) -> None:
    assert sort_by_date(sample_list_of_data_base_executed_without_state) == sample_list_of_data_base_sorted_by_date


def test_sort_by_date_reverse(
    sample_list_of_data_base_executed_without_state: list,
    ascending_false: bool,
    sample_list_of_data_base_sorted_by_date_reverted: list,
) -> None:
    assert (
        sort_by_date(sample_list_of_data_base_executed_without_state, ascending_false)
        == sample_list_of_data_base_sorted_by_date_reverted
    )
