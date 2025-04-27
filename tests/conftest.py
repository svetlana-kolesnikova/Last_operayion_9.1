import pytest

@pytest.fixture
def digit_number_wrong():
    return "700079228960636"

@pytest.fixture
def digit_alpha_number_wrong():
    return "card1234_alpha"
