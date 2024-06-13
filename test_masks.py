import pytest

from src.masks import mask_card_number, mask_account_number


@pytest.fixture
def private_card_number() -> str:
    return "7000 7922 8960 6361"


@pytest.fixture
def private_account_number() -> str:
    return "64686473678894779589"


def tests_mask_card_number(private_card_number: str) -> None:
    assert mask_card_number(private_card_number) == "7000  7** **** 6361"


def tests_mask_account_number(private_account_number: str) -> None:
    assert mask_account_number(private_account_number) == "**9589"
