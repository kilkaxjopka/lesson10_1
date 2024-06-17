import pytest
from src.widget import mask_number, refactor_the_date


@pytest.fixture
def date() -> str:
    return "2018-07-11T02:26:18.671407"


def test_refactor_the_date(date: str) -> None:
    assert refactor_the_date(date) == "11.07.2018"


@pytest.mark.parametrize(
    "number, result",
    [

        ("Visa Platinum 7000 7922 8960 6361", "Visa Platinum 7000 79** **** 6361"),
        ("Maestro 1596837868705199", "Maestro 1596 83** **** 5199"),
        ("Счет 64686473678894779589", "Счет **9589"),

    ],
)
def test_mask_number(number: str, result: str) -> None:
    assert mask_number(number) == result
