from typing import Any
from unittest.mock import mock_open, patch

from src.utils import read_json


@patch("json.load", return_value=[{"key": "value"}])
@patch("builtins.open", new_callable=mock_open, read_data='[{"key": "value"}]')
def test_read_json_with_patch(mock_file: Any, mock_json: Any) -> Any:
    """Тест при наличии корректного файла .json"""
    result = read_json("fake_file.json")
    assert result == [{"key": "value"}]
    mock_file.assert_called_once_with("fake_file.json", encoding="utf-8")
    mock_json.assert_called_once()


def test_read_json_file_not_found() -> Any:
    """Тест при отсутствии файла .json"""
    result = read_json("non_existent_file.json")
    assert result == []


def test_read_json_invalid_json(tmp_path: Any) -> Any:
    """Тест при некорректном файле .json"""
    bad_file = tmp_path / "bad.json"
    bad_file.write_text("{ invalid json }", encoding="utf-8")

    result = read_json(bad_file)
    assert result == []


def test_read_json_empty_file(tmp_path: Any) -> Any:
    """Тест при пустом файле .json"""
    empty_file = tmp_path / "empty.json"
    empty_file.write_text("", encoding="utf-8")

    result = read_json(empty_file)
    assert result == []
